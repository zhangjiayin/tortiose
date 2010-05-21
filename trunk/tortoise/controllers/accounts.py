#-*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from tortoise.lib.base import BaseController, render

from pylons.decorators import validate
from pylons import session
from tortoise.model.form import *

log = logging.getLogger(__name__)

class AccountsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/accounts.mako')
        # or, return a response
        return 'Hello World'

    def newaccount(self):
        return render('accounts/newaccount.html')

    @validate(schema=NewAccountForm(), form='newaccount', post_only=False, on_get=True,auto_error_formatter=account_formatter)
    def createaccount(self):
        response.write(request.method)
        response.write(str(request.params.get('email')))
        response.write(str(request.POST.has_key('aaa')))

    def login(self):
        return render('accounts/login.html')

    @validate(schema=LoginForm(), form='login', post_only=False, on_get=True,auto_error_formatter=account_formatter)
    def loginauth(self):
        response.write(str(request.params.get('email')))
        response.write(str(request.POST.has_key('password')))

