import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from tortoise.lib.base import BaseController, render

log = logging.getLogger(__name__)

class AccountsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/accounts.mako')
        # or, return a response
        return 'Hello World'
    def newaccount(self):
        return render('accounts/newaccount.html');
