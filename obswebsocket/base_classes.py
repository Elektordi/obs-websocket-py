#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy


class Baseevents:
    def __init__(self):
        self.name = '?'
        self.datain = {}

    def input(self, data):
        r = copy.copy(data)
        del r['update-type']
        self.datain = r

    def __repr__(self):
        return u"<{} event ({})>".format(self.name, self.datain)


class Baserequests:
    def __init__(self):
        self.name = '?'
        self.datain = {}
        self.dataout = {}
        self.status = None

    def data(self):
        payload = copy.copy(self.dataout)
        payload.update({'request-type': self.name})
        return payload

    def input(self, data):
        r = copy.copy(data)
        del r['message-id']
        self.status = (r['status'] == 'ok')
        del r['status']
        self.datain = r

    def __repr__(self):
        if self.status is None:
            return u"<{} request ({}) waiting>".format(self.name, self.dataout)
        elif self.status:
            return u"<{} request ({}) called: success ({})>".format(
                self.name, self.dataout, self.datain)
        else:
            return u"<{} request ({}) called: failed ({})>".format(
                self.name, self.dataout, self.datain)
