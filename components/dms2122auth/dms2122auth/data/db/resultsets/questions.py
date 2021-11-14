""" Questions class module.
"""

import hashlib
from typing import List
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2122auth.data.db.results import Question
from dms2122auth.data.db.exc import UserExistsError

class Questions():
    """ Class Question. (no utilizada en esta entrega)
    """
    @staticmethod
    def list_all(session: Session) -> List[Question]:
        """ Gets the list of questions from the database.

        Args:
            - session (Session): The session object.

        Returns:
            - List: A list object with the questions.
        """
        query = session.query(Question)
        return query.all()


   