#-*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from tortoise.lib.base import BaseController, render

from pylons.decorators import validate
from pylons import session
from tortoise.model.form import *
from tortoise.model import meta
from tortoise.model.account import *

log = logging.getLogger(__name__)

class AccountsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/accounts.mako')
        # or, return a response
        return 'Hello World'

    def newaccount(self):
        if request.params.get("error"):
            key = request.params.get('error')
            c.error = key 
            c.message = common_messages[key]

        return render('accounts/newaccount.html')

    @validate(schema=NewAccountForm(), form='newaccount', post_only=False, on_get=True,auto_error_formatter=account_formatter)
    def createaccount(self):
        account_mode = AccountModel()

        response.write(str(account_mode.checkMailExists(request.params.get('email'))))
        response.write(request.method)
        response.write(str(request.params.get('email')))
        response.write(str(request.POST.has_key('aaa')))

    def login(self):
        return render('accounts/login.html')

    @validate(schema=LoginForm(), form='login', post_only=False, on_get=True,auto_error_formatter=account_formatter)
    def loginauth(self):
        response.write(str(request.params.get('email')))
        response.write(str(request.POST.has_key('password')))

    def checkUserExists(self):
        return 'Noting'

