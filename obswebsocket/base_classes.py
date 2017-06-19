#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

class BaseEvent:
    def __init__(self):
        self.name = "?"
        self.dataout = {}
        
    def input(self, data):
        r = copy.copy(data)
        del r['update-type']
        self.dataout = r
        
    def __repr__(self):
        return "<%s event (%r)>"%(self.name, self.dataout)
        
    
class BaseRequest:
    def __init__(self):
        self.name = "?"
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
        self.status = (r['status']=="ok")
        del r['status']
        self.dataout = r
        
    def __repr__(self):
        if self.status is None:
            return "<%s request (%r) waiting>"%(self.name, self.dataout)
        elif self.status:
            return "<%s request (%r) called: success (%r)>"%(self.name, self.dataout, self.datain)
        else:
            return "<%s request (%r) called: failed (%r)>"%(self.name, self.dataout, self.datain)
            
