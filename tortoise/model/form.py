# -*- coding: utf-8 -*- 
import formencode
import re
from formencode import htmlfill
from formencode.schema import Schema
from formencode.validators import Invalid, FancyValidator
from formencode.validators import Int, DateConverter, String, OneOf
from formencode import variabledecode
from formencode import htmlfill
from formencode.foreach import ForEach
from formencode.api import NoDefault

common_messages ={ 
        'empty': u'不能为空',
        'badType': u'必须输入一个字符串(不能是 %(type)s: %(value)r)',
        }

class SecurePassword(formencode.validators.FancyValidator):
    min = 6
    non_letter = 3
    letter_regex = re.compile(r'[a-zA-Z]')
    messages = {
            'too_few': u'安全起见，您的密码长度设置时 必须大于 %(min)i 个字符',
            'non_letter': u'安全起见，您的密码必须包含 %(non_letter)i 个字符([a-zA-c])',
            }

    def _to_python(self, value, state):
        # _to_python gets run before validate_python.  Here we
        # strip whitespace off the password, because leading and
        # trailing whitespace in a password is too elite.
        return value.strip()

    def validate_python(self, value, state):
        if len(value) < self.min:
            raise Invalid(self.message("too_few", state,
                min=self.min),
                value, state)
        non_letters = self.letter_regex.sub('', value)
        if len(non_letters) < self.non_letter:
            raise Invalid(self.message("non_letter",
                non_letter=self.non_letter),
                value, state)

class NewAccountForm(Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    email = formencode.validators.Email(not_empty=True)
    password = SecurePassword()
    password_confirm = String(not_empty=True)

    chained_validators = [formencode.validators.FieldsMatch('password', 'password_confirm')]

    nickname           = String(not_empty=True)

def account_formatter(error):
        return '<div class="error">%s</div>' % ( htmlfill.html_quote(error))

class LoginForm(Schema):
    email = formencode.validators.Email(not_empty=True)
    password        = String(not_empty=True)


