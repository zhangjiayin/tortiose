# -*- coding: utf-8 -*-
"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render

from tortoise.model import meta

from pylons.decorators import validate

import socket, struct

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            meta.Session.remove()



def ip2long(ip):
    "convert decimal dotted quad string to long integer"
    return struct.unpack('L',socket.inet_aton(ip))[0]

def long2ip(n):
    "convert long int to dotted quad string"
    return socket.inet_ntoa(struct.pack('L',n))
def makeMask(n):
    "return a mask of n bits as a long integer"
    return (2L<<n-1)-1
def ipToNetAndHost(ip, maskbits):
    "returns tuple (network, host) dotted-quad addresses given IP and mask size"
    #(by Greg Jorgensen)
    n = ip2long(ip)
    m = makeMask(maskbits)
    host = n & m
    net = n - host
    return long2ip(net), long2ip(host)

