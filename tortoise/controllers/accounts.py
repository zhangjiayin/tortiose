#-*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from tortoise.lib.base import BaseController, render, ip2long

from pylons.decorators import validate
from pylons import session
from tortoise.model.form import *
from tortoise.model import meta
from tortoise.model.account import *

import uuid, hashlib,time

from pylons import session
from pylons import config

import socket, struct
import formencode

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
        if  not (UserBase.checkMailExists(request.params.get('email'))):
	    userBase = UserBase()
	    userBase.id = uuid.uuid4()
	    userBase.email = request.params.get('email')
	    userBase.nick = request.params.get('nick').encode('utf8')

	    userBase.password = hashlib.md5(request.params.get('password')).hexdigest()
	    userBase.register_time = int(time.time())

	    userBase.register_ip = ip2long(request.environ.get("X_FORWARDED_FOR", request.environ["REMOTE_ADDR"]))

	    meta.Session.add(userBase)
	    meta.Session.flush()
            session[config['auth_user_id']] = userBase.id
            session['auth_user'] = userBase
            session.save()
	    redirect_to('/')
	else:
	    redirect_to(controller='accounts', action='newaccount', _code=303, error="mail_exist")


    def login(self):
        return render('accounts/login.html')

    @validate(schema=LoginForm(), form='login', post_only=False, on_get=True,auto_error_formatter=account_formatter)
    def loginauth(self):
        userBase = UserBase.auth(request.params.get('email'),hashlib.md5(request.params.get('password')).hexdigest())
        if(userBase):
            session[config['auth_user_id']] = userBase.id
            session['auth_user'] = userBase
            session.save()
	    redirect_to('/')
        else:
	    redirect_to(controller='accounts', action='login', _code=303, error="login_error")

    def logout(self):
        session.delete()
        redirect_to('/')
    def checkUserExists(self):
        return 'Noting'

