
#!/usr/bin/env python3

import hashlib
import uuid
from sqlalchemy.orm.session import Session
from schema import Schema
from results import User, UserSession

def test():
    """
    >>> from schema import Schema
    >>> from results import User, UserSession
    >>> schema = Schema('sqlite:///:memory:')
    >>> usr1 = User('User1', 'usr1pass')
    >>> usr2 = User('User2', 'usr2pass')
    >>> session1_1 = UserSession('12345678-1234-1234-1234-123456789012', 'User1')
    >>> db_session = schema.new_session()
    >>> db_session.add_all([usr1, usr2, session1_1])
    >>> db_session.commit()
    >>> for instance in db_session.query(User).order_by(User.username):
    ...     print (instance.username, instance.password)
    User1 usr1pass
    User2 usr2pass
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()