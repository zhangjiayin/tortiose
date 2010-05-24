import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from tortoise.lib.base import BaseController, render

log = logging.getLogger(__name__)

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import RemoteUser, ValidAuthKitUser, UserIn

class AuthController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/auth.mako')
        # or, return a response
        return 'Hello World'
    @authorize(RemoteUser())
    def private(self):
        return "You are not authenticated"
    def signout(self):
        return "Successfully signed out!"
