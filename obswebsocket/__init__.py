#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python library to communicate with an obs-websocket server.
"""

from . import core

class obsws:
    """
    Wrapper class for using obs-websocket-py
    
    Simple usage:
        >>> import obswebsocket, obswebsocket.requests
        >>> client = obswebsocket.obsws("localhost", 4444, "secret")
        >>> client.connect()
        >>> client.call(obswebsocket.requests.GetVersion()).getObsWebsocketVersion()
        u'4.1.0'
        >>> client.disconnect()
        
    For advanced usage, including events callback, see the 'samples' directory. 
    """
    
    def __init__(self, host, port = 4444, password = ''):
        """
        Construct a new obsws wrapper
        
        :param host: Hostname to connect to
        :param port: TCP Port to connect to (Default is 4444)
        :param password: Password for the websocket server (Leave this field empty if no auth enabled
            on the server)
        """
        self.host = host
        self.port = port
        self.password = password

        self._core = core.Core()

    def connect(self):
        """
        Connect to the websocket server
        
        :return: Nothing
        """
        self._core.connect(self.host, self.port)
        self._core.auth(self.password)
        self._core.run_threads()

    def disconnect(self):
        """
        Disconnect from websocket server
        
        :return: Nothing
        """    
        self._core.disconnect()

    def register(self, function, event = None):
        """
        Register a new hook in the websocket client
        
        :param function: Callback function pointer for the hook
        :param event: Event (class from obswebsocket.events module) to trigger the hook on.
            Default is None, which means trigger on all events.
        :return: Nothing
        """
        self._core.eventmanager.register(function, event)

    def unregister(self, function, event = None):
        """
        Unregister a new hook in the websocket client
        
        :param function: Callback function pointer for the hook
        :param event: Event (class from obswebsocket.events module) which triggered the hook on.
            Default is None, which means unregister this function for all events.
        :return: Nothing
        """
        self._core.eventmanager.unregister(function, event)

    def call(self, obj):
        """
        Make a call to the OBS server through the Websocket.
        
        :param obj: Request (class from obswebsocket.requests module) to send to the server.
        :return: Request object populated with response data.
        """
        return self._core.call(obj)

    def send(self, data):
        """
        **DEPRACATED***
        Make a raw json call to the OBS server through the Websocket.
        
        :param obj: Request (python dict) to send to the server. Do not include field "message-id".
        :return: Response (python dict) from the server.
        """
        return self._core.send(data)

