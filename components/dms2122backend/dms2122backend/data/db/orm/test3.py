
#!/usr/bin/env python3

import hashlib
import uuid
from sqlalchemy.orm.session import Session
from schema import Schema
from results import Answer, Question, User

def test():
    """
    >>> from schema import Schema
    >>> from results import Question, Answer, User
    >>> schema = Schema('sqlite:///:memory:')
    >>> quest1 = Question('1', 'usr1pass','2', '2', '2', '3', '4', '1' , 'User1')
    >>> quest2 = Question('2', 'usr1pass','2', '2', '2', '3', '4', '1', 'user2')
    >>> usr1 = User('User1', 'usr1pass')
    >>> answer1 = Answer('1', '1', '2', '4', 'User1')
    >>> db_session = schema.new_session()
    >>> db_session.add_all([quest1, quest2, usr1, answer1])
    >>> db_session.commit()
    >>> for instance in db_session.query(Question).order_by(Question.id):
    ...     print (instance.userCreated)
    User1
    user2
    """

    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()