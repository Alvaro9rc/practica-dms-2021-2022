#!/usr/bin/env python3

import hashlib
import uuid
from sqlalchemy import create_engine, Table, MetaData, Column, String, ForeignKey  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker, mapper, relationship  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore

declarative_base_class = declarative_base()
engine = create_engine('sqlite:////tmp/database.db')
session_maker = sessionmaker(bind=engine)

users_table = Table('users', declarative_base_class.metadata,
    Column('username', String(32), primary_key=True),
    Column('password', String(64), nullable=False)
)

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

user_sessions_table = Table('user_sessions', declarative_base_class.metadata,
    Column('token', String(36), primary_key=True),
    Column('username', String(32), ForeignKey('users.username'), nullable=False)
)

class UserSession():
    def __init__(self, token, username):
        self.token = token
        self.username = username

mapper(User, users_table, properties={'sessions': relationship(UserSession, backref='users')})
mapper(UserSession, user_sessions_table)

declarative_base_class.metadata.create_all(engine)

usr1 = User("User1", hashlib.sha256(bytes('usr1pass', 'utf-8')).hexdigest())
usr2 = User("User2", hashlib.sha256(bytes('usr2pass', 'utf-8')).hexdigest())
session1_1 = UserSession(str(uuid.uuid4()), "User1")

db_session = session_maker()
db_session.add_all([usr1, usr2, session1_1])
db_session.commit()