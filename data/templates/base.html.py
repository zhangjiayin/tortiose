# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274788891.492126
_template_filename=u'/usr/code/pylons/tortoise/tortoise/templates/base.html'
_template_uri=u'/base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n    <head>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        # SOURCE LINE 6
        if hasattr(self, 'title'):
            # SOURCE LINE 7
            __M_writer(u'        <title>')
            __M_writer(escape(self.title()))
            __M_writer(u'</title>\n')
            pass
        # SOURCE LINE 9
        __M_writer(u'        ')
        __M_writer(escape(h.stylesheet_link('/css/screen.css',  media="screen, projection")))
        __M_writer(u'\n        ')
        # SOURCE LINE 10
        __M_writer(escape(h.stylesheet_link('/css/print.css',  media="screen")))
        __M_writer(u'\n        ')
        # SOURCE LINE 11
        __M_writer(escape(h.stylesheet_link('/css/print.css',  media="screen")))
        __M_writer(u'\n        <!--[if lt IE 8]><link rel="stylesheet" href="/css/ie.css" type="text/css" media="screen, projection"><![endif]-->\n\n')
        # SOURCE LINE 14
        if hasattr(self, 'css'):
            # SOURCE LINE 15
            __M_writer(u'        ')
            __M_writer(escape(self.css()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 17
        __M_writer(u'\n        ')
        # SOURCE LINE 18
        __M_writer(escape(h.javascript_link('/js/common/jquery.js')))
        __M_writer(u'\n        ')
        # SOURCE LINE 19
        __M_writer(escape(h.javascript_link('/js/common/common.js')))
        __M_writer(u'\n')
        # SOURCE LINE 20
        if hasattr(self, 'js'):
            # SOURCE LINE 21
            __M_writer(u'        ')
            __M_writer(escape(self.js()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 23
        __M_writer(u'    </head>\n    <body>\n        <div class="span-24"><a href="/">\u5230\u9996\u9875</a></div>\n        ')
        # SOURCE LINE 26
        __M_writer(escape(self.body()))
        __M_writer(u'\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


