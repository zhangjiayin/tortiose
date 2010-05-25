#-*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect, redirect_to

from tortoise.lib.base import BaseController, render

from tortoise.model.form import *
from tortoise.model import meta
from tortoise.model.account import *
from pylons.decorators import validate
import formencode
from pylons import session
import logging
from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
from tortoise.lib.base import BaseController, render, ip2long
from pylons.decorators import validate


import json

from tortoise.lib.pyrfeed.GoogleReader import *

from tortoise.lib.auth import *

import webhelpers.paginate
from webhelpers import pagination

from pylons import config

log = logging.getLogger(__name__)

class UController(BaseController):

    @require_login
    def index(self, id=None):
        # Return a rendered template
        #return render('/u.mako')
        # or, return a response
        userBase = UserBase.getUserBaseById(session[config['auth_user_id']])
        userProfile = UserProfile.getUserProfileById(userBase.id)
        """
        if userProfile != None  and userProfile.google_account:
            google_account = json.loads(userProfile.google_account)
            c.google_account = google_account
            gr = GoogleReader()
            gr.identify(google_account['email'], google_account['email'])
            if gr.login():
                c.logined = True
            else:
                c.logined = False
        """
        c.userProfile = userProfile
        c.userBase  = userBase

        c.paginate = webhelpers.paginate.Page(
                  UserSubscribe.getSubscribeByUser(get_auth_id()),
                  page = int(request.params.get('page',1)),
                  items_per_page = 10)

        c.subscribes = []

        for subscribe in c.paginate:
            r = {}
            s = FeedSource.getFeedSourceById(subscribe.source_id)
            r['id'] = subscribe.id
            r['name'] = s.name
            r['url'] = s.url
            r['add_time'] = subscribe.add_time
            c.subscribes.append(r);



        return render('/u/index.html')
    
    @require_login
    @validate(schema=RelatingGoogleForm(), form='index', post_only=False, on_get=True,auto_error_formatter=account_formatter)
    def relating(self, id=None):
        if id == None or (not 'auth_user_id' in session) or session['auth_user_id'] == None:
            return redirect_to(controller='accounts', action='login')

        userBase = UserBase.getUserBaseById(session['auth_user_id'])
        userProfile = UserProfile.getUserProfileById(userBase.id)

        if(userProfile == None):
            userProfile = UserProfile()
            userProfile.id = userBase.id

        google_account = unicode(json.dumps({'email':request.params.get('email'), 'password':request.params.get('password')}))
        userProfile.google_account = google_account

        meta.Session.add(userProfile)
        meta.Session.commit()

        return redirect_to(controller='u', action='index',id = session['auth_user_id'])
