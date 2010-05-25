#-*- coding: utf-8 -*-
__all__ = ["get_auth_id", "require_login", 'require_login_json']

from pylons.controllers.util import abort, redirect_to, url_for
from pylons import session
from pylons import config

def get_auth_id():
    if config['auth_user_id'] in session and session[config['auth_user_id']] != None:
        return session[config['auth_user_id']]
    else:
        return None

def require_login(func):
    """ Checks to see if user_id is in session """
    if get_auth_id() == None:
        def dfunc(*args, **kwargs):
            redirect_to(config['login_url'])
        return dfunc
    else:
        return func

def require_login_json(func):
    """ Checks to see if user_id is in session """
    if get_auth_id() == None:
        def dfunc(*args, **kwargs):
            return {'error':403};
        return dfunc
    else:
        return func
