import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from tortoise.lib.base import BaseController, render

from pylons import session

log = logging.getLogger(__name__)

class IndexController(BaseController):

    def index(self):
        response.write(str(type(session['user'])))

        if ('user' in session) and session['user'] != None:
            response.write(session['user'].email)
            response.write('<br />')
            response.write(str(session['user'].nick))
            response.write('<br />')
            response.write(str(session['user'].id))
        else:
            response.write('not login')
