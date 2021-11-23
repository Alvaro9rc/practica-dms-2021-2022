
#!/usr/bin/env python3

import hashlib
import uuid
from sqlalchemy.orm.session import Session
from schema import Schema
from results import Question, Answer

def test():
    """
    >>> from schema import Schema
    >>> from results import Question, Answer
    >>> schema = Schema('sqlite:///:memoryAnswer:')
    >>> question1 = Question("1","¿Cuántos años tiene John Lenon?",  "hay que tener un poco de cultura general", "23", "45", "89", "10", "5")
    >>> question2 = Question("2","¿Cuántos años tiene Michael Jackson?",  "hay que tener un poco de cultura general", "2344", "Esta muerto", "89", "20", "10")
    >>> Answer1 = Answer('1', 1, '2', '10')
    >>> Answer2 = Answer('2', 2, '1', '20')
    >>> db_session = schema.new_session()
    >>> db_session.add_all([question1, question2, Answer1)
    >>> db_session.commit()
    >>> for instance in db_session.query(Question).order_by(Question.id):
    ...     print (instance.id)
    1
    2
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()