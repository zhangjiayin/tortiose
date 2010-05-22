# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274520149.1400001
_template_filename='/development/tortiose/tortoise/templates/accounts/newaccount.html'
_template_uri='accounts/newaccount.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'')
        # SOURCE LINE 3
        __M_writer(u'\n<div class="container showgrid">\n    <h1>Create New Account</h1>\n    <hr>\n    <div class="span-24">\n        <form action="/accounts/createaccount" method="post">\n            <fieldset>\n                <legend>submit your infomation</legend>\n                <label for="dummy0">you email</label><br>\n                <div class="span-24">\n                    <div class="span-10">\n                        <input type="text" class="title" name="email" id="email" value="" />\n                    </div>\n                    <div class="span-13">\n')
        # SOURCE LINE 17
        if c.error == "mail_exist":
            # SOURCE LINE 18
            __M_writer(u'                        <div class="error">\n                          ')
            # SOURCE LINE 19
            __M_writer(escape(c.message))
            __M_writer(u'\n                        </div>\n')
            pass
        # SOURCE LINE 22
        __M_writer(u'                        <div class="notice hide">\n                            This is a &lt;div&gt; with the class <strong>.notice</strong>. <a href="#">Link</a>.\n                        </div>\n                        <div class="success hide">\n                            This is a &lt;div&gt; with the class <strong>.success</strong>. <a href="#">Link</a>.\n                        </div>\n                    </div>\n                </div>\n\n                <label for="dummy1">your password</label><br>\n                <div class="span-24">\n                    <div class="span-10">\n                        <input type="password" class="text" id="password" name="password" value="" />\n                    </div>\n                    <div class="span-13">\n                        <div class="error hide">\n                            This is a &lt;div&gt; with the class <strong>.error</strong>. <a href="#">Link</a>.\n                        </div>\n                        <div class="notice hide">\n                            This is a &lt;div&gt; with the class <strong>.notice</strong>. <a href="#">Link</a>.\n                        </div>\n                        <div class="success hide">\n                            This is a &lt;div&gt; with the class <strong>.success</strong>. <a href="#">Link</a>.\n                        </div>\n                    </div>\n                </div>\n\n                <label for="dummy1">confirm your password</label><br>\n                <div class="span-24">\n                    <div class="span-10">\n                        <input type="password" class="text" id="password_confirm" name="password_confirm" value="" />\n                    </div>\n                    <div class="span-13">\n                        <div class="error hide">\n                            This is a &lt;div&gt; with the class <strong>.error</strong>. <a href="#">Link</a>.\n                        </div>\n                        <div class="notice hide">\n                            This is a &lt;div&gt; with the class <strong>.notice</strong>. <a href="#">Link</a>.\n                        </div>\n                        <div class="success hide">\n                            This is a &lt;div&gt; with the class <strong>.success</strong>. <a href="#">Link</a>.\n                        </div>\n                    </div>\n                </div>\n\n                <label for="dummy1">your nickname</label><br>\n                <div class="span-24">\n                    <div class="span-10">\n                        <input type="text" class="text" id="nick" name="nick" value=""/>\n                    </div>\n                    <div class="span-13">\n                        <div class="error hide">\n                            This is a &lt;div&gt; with the class <strong>.error</strong>. <a href="#">Link</a>.\n                        </div>\n                        <div class="notice hide">\n                            This is a &lt;div&gt; with the class <strong>.notice</strong>. <a href="#">Link</a>.\n                        </div>\n                        <div class="success hide">\n                            This is a &lt;div&gt; with the class <strong>.success</strong>. <a href="#">Link</a>.\n                        </div>\n                    </div>\n                </div>\n                <p>\n                <input type="submit" value="Submit">\n                <input type="reset" value="Reset">\n                </p>\n            </fieldset>\n        </form>\n    </div>\n    <div class="span-12 last">\n    </div>\n    <hr>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Create New Account')
        return ''
    finally:
        context.caller_stack._pop_frame()


