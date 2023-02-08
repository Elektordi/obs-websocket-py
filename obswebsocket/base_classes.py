import copy
import re

camelcase_to_kebabcase = re.compile(r'(?<!^)(?=[A-Z])')


class Baseevents:
    def __init__(self):
        self.name = type(self).__dict__.get('name') or "?"
        self.datain = {}

    def input(self, data):
        r = copy.copy(data)
        self.datain = r

    def __repr__(self):
        return u"<{} event ({})>".format(self.name, self.datain)

    def __getattr__(self, item):
        if item.startswith("get"):
            def getter():
                key1 = key = item[3:4].lower() + item[4:]
                if key not in self.datain:
                    key = camelcase_to_kebabcase.sub('-', key).lower()
                if key not in self.datain:
                    raise KeyError(key1)
                return self.datain[key]
            return getter
        raise AttributeError("'{}' object has no attribute '{}'".format(self.name, item))


class Baserequests:
    def __init__(self, **kwargs):
        self.name = type(self).__dict__.get('name') or "?"
        self.datain = {}
        self.dataout = {}
        for k in kwargs:
            self.dataout[k] = kwargs[k]
        self.status = None

    def data(self):
        payload = copy.copy(self.dataout)
        return payload

    def input(self, data, status):
        r = copy.copy(data)
        self.datain = r
        self.status = status

    def __repr__(self):
        if self.status is None:
            return u"<{} request ({}) waiting>".format(self.name, self.dataout)
        elif self.status:
            return u"<{} request ({}) called: success ({})>".format(self.name, self.dataout, self.datain)
        else:
            return u"<{} request ({}) called: failed ({})>".format(self.name, self.dataout, self.datain)

    def __getattr__(self, item):
        if item.startswith("get"):
            def getter():
                key1 = key = item[3:4].lower() + item[4:]
                if key not in self.datain:
                    key = camelcase_to_kebabcase.sub('-', key).lower()
                if key not in self.datain:
                    raise KeyError(key1)
                return self.datain[key]
            return getter
        raise AttributeError("'{}' object has no attribute '{}'".format(self.name, item))


class ClassFactory:
    cache = {}

    def __init__(self, base_class):
        self.base_class = base_class

    def __getattr__(self, item):
        new_class = ClassFactory.cache.get((self.base_class, item))
        if not new_class:
            new_class = type(item, (self.base_class,), {})
            new_class.name = item
            ClassFactory.cache[(self.base_class, item)] = new_class
        return new_class
