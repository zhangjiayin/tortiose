#-*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from tortoise.lib.base import BaseController, render

from pylons import session

log = logging.getLogger(__name__)

class IndexController(BaseController):

    def index(self):
        if 'auth_user_id' in session:
            redirect_to(controller='u', action='index', id=session['auth_user_id'])
        else:
	    redirect_to(controller='accounts', action='login', _code=302)
