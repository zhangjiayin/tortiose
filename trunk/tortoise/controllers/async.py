import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from tortoise.lib.base import BaseController, render

from pylons.decorators import jsonify

from tortoise.model.form import *
from tortoise.model import meta
from tortoise.model.account import *


from tortoise.lib.auth import *
import time
import hashlib

log = logging.getLogger(__name__)

class AsyncController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/async.mako')
        # or, return a response
        return 'Hello World'

    @jsonify
    @require_login_json
    def subscribe(self):
        r = {'error':200}
        url = request.params.get("url",None)
        if url == None:
            r['error'] = 404
            return r

        source_id = hashlib.md5(url).hexdigest()
        r['id'] = source_id

        source = FeedSource.getFeedSourceById(source_id)
        current = int(time.time())
        if source == None:
            source = FeedSource()
            source.id = source_id
            source.url = url
            source.name = ""
            source.add_time = current
            source.update_time = current
            meta.Session.add(source)
            source.init()

        userSubscribe = UserSubscribe.getUserSubscribeById(get_auth_id(), source_id)

        if userSubscribe == None:
            subscribe = UserSubscribe()
            subscribe.id = get_auth_id()
            subscribe.source_id = source_id
            subscribe.add_time = current
            meta.Session.add(subscribe)

        meta.Session.flush()

            
        r['url'] = url
        return r

