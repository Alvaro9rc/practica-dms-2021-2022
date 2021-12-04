""" Answers class module.
"""

import hashlib
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2122backend.data.db.results import Answer
from dms2122backend.data.db.exc.questionexisterror import QuestionExistsError
from dms2122backend.data.db.exc.questionnotfounderror import QuestionNotFoundError
from dms2122auth.data.db.exc.usernotfounderror import UserNotFoundError

class Answers():
    """ Class responsible of table-level answers operations.
    """
    @staticmethod
    def create_answer(session: Session, id: int, questionId: int, answer: str, valoration: float, username: str) -> Answer:
        """ creates an answer given to a question.
        Note:
            Any existing transaction will be committed.
        Args:
            - session (Session): The session object.
            - id: answer id.
            - question: question id.
            - answer: answer qiven.
            - valoration: puntuation gotten from the answer.
            - username: user who answered.
        Raises:  
            - ValueError: If any field is empty.
            - UserNotFoundError: If the user does not exist.
            - QuestionNotFoundError: If the question answered does not exist.
        Returns:
            - Answer: The answer to the question
        """
        if not id or not questionId or not answer or not valoration or not username:
            raise ValueError('All fields are required.')
        try:
            new_answer = Answer(id, questionId, answer, valoration, username)
            session.add(new_answer)
            session.commit()
            return new_answer
        except IntegrityError as ex:
            session.rollback()
            raise QuestionNotFoundError() from ex 
        except:
            session.rollback()
            raise

    @staticmethod
    def list_all(session: Session) -> List[Answer]:
        """Lists every answer.
        Args:
            - session (Session): The session object.
        Returns:
            - List[Answer]: A list of answers registers.
        """
        query = session.query(Answer)
        return query.all()

    @staticmethod
    def list_all_by_user(session: Session, user: str) -> List[Answer]:
        """Lists all the answers given by a user.
        Args:
            - session (Session): The session object.
            - user (str): The user name string.
        Raises:
            - ValueError: If the username is missing.
        Returns:
            - List[Answer]: All the answers given by that user.
        """
        if not user:
            raise ValueError('A username is required.')
        query = session.query(Answer).filter_by(user=user)
        return query.all()

    @staticmethod
    def list_all_by_question(session: Session, questionId: int) -> List[Answer]:
        """Lists all the answers given to a question.
        Args:
            - session (Session): The session object.
            - questionId (int): The question id.
        Raises:
            - ValueError: If the question id is missing.
        Returns:
            - List[Answer]: A list of answers to the question.
        """
        if not id:
            raise ValueError('A question id is required.')
        query = session.query(Answer).filter_by(questionId=questionId )
        return query.all()
