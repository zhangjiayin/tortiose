#-*- coding: utf-8 -*-
"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.sql import and_

from tortoise.model import meta


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine


## Non-reflected tables may be defined and mapped at module level
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)

user_table = sa.Table("user",meta.metadata,
        sa.Column("id", sa.types.String(40), primary_key=True),
        sa.Column("email", sa.types.String(50), nullable=False),
        sa.Column("nick", sa.types.String(50), nullable=False),
        sa.Column("password", sa.types.String(32), nullable=False),
        sa.Column("register_time", sa.types.Integer, nullable=False),
        sa.Column("register_ip", sa.types.Integer, nullable=False),
        )

user_profile_table = sa.Table("user_profile", meta.metadata,
        sa.Column("id", sa.types.String(40), primary_key=True),
        sa.Column("birthday", sa.types.DateTime, nullable=False),
        sa.Column("carrer", sa.types.UnicodeText, nullable=False),
        sa.Column("google_account", sa.types.UnicodeText, nullable=False),
        )

user_subscribe_table = sa.Table("user_subscribe", meta.metadata,
        sa.Column("id", sa.types.String(40), primary_key=True),
        sa.Column("source_id", sa.types.String(40), nullable=False),
        sa.Column("add_time", sa.types.Integer, nullable=False),
        sa.schema.PrimaryKeyConstraint('id', 'source_id'),
)


feed_source_table = sa.Table("feed_source", meta.metadata,
        sa.Column("id", sa.types.String(32), primary_key=True),
        sa.Column("name", sa.types.String(20), nullable=False),
        sa.Column("url", sa.types.String(255), nullable=False),
        sa.Column("add_time", sa.types.Integer, nullable=False),
        sa.Column("update_time", sa.types.Integer, nullable=False),

        )

class UserBase(object):

    query = None

    def __str__(self):
        return self.nick
    def __repr__(self):
        return self.nick
    @classmethod
    def getQuery(cls):
        if cls.query == None:
            cls.query = meta.Session.query(UserBase)
        return cls.query

    @classmethod
    def checkMailExists(cls, email):
	return cls.getQuery().filter(UserBase.email==email).count() > 0

    @classmethod
    def auth(cls, email, password):
        u = cls.getQuery().filter(and_(UserBase.email==email)).first()

        if u != None and u.password == password:
            return u
        else:
            return None

    @classmethod
    def getUserBaseById(cls, id):
        return cls.getQuery().filter(and_(UserBase.id==id)).first()

class UserProfile(object):
    query = None
    def __init__(self):
        self.id = ''
        self.birthday = ''
        self.carrer = ''
        self.google_account = ''

    @classmethod
    def getQuery(cls):
        if cls.query == None:
            cls.query = meta.Session.query(UserProfile)
        return cls.query

    @classmethod
    def getUserProfileById(cls, id):
        return cls.getQuery().filter(UserProfile.id==id).first()

class UserSubscribe(object):
    query = None

    @classmethod
    def getQuery(cls):
        if cls.query == None:
            cls.query = meta.Session.query(UserSubscribe)
        return cls.query

    @classmethod
    def getUserSubscribeById(cls, id, source_id):
        return cls.getQuery().filter(and_(UserSubscribe.id==id, UserSubscribe.source_id==source_id)).first()

    @classmethod
    def getSubscribeByUser(cls,id):
        q = cls.getQuery().filter(and_(UserSubscribe.id==id))
        q.order_by(UserSubscribe.add_time.desc())
        return q.all()

class FeedSource(object):

    query = None

    @classmethod
    def getQuery(cls):
        if cls.query == None:
            cls.query = meta.Session.query(FeedSource)
        return cls.query

    @classmethod
    def getFeedSourceById(cls, id):
        return cls.getQuery().filter(FeedSource.id==id).first()

    def init(self):
        pass

#user_subscribe

orm.mapper(UserBase, user_table)
orm.mapper(UserProfile, user_profile_table)
orm.mapper(UserSubscribe, user_subscribe_table)

orm.mapper(FeedSource, feed_source_table)



## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
