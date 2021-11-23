#!/usr/bin/env python3

import hashlib
import uuid
from sqlalchemy.orm.session import Session
from schema import Schema
from results import User, UserSession

schema: Schema = Schema('sqlite:////tmp/database.db')
usr1: User = User("User1", hashlib.sha256(bytes('usr1pass', 'utf-8')).hexdigest())
usr2: User = User("User2", hashlib.sha256(bytes('usr2pass', 'utf-8')).hexdigest())
session1_1: UserSession = UserSession(str(uuid.uuid4()), "User1")

db_session: Session = schema.new_session()
db_session.add_all([usr1, usr2, session1_1])
db_session.commit()