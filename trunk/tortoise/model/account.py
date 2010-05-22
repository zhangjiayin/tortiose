from tortoise.model import meta
from tortoise.model import *
class AccountModel:
    def checkMailExists(self, email):
	user_q = meta.Session.query(UserBase)
	return user_q.filter(UserBase.email==email).one()
