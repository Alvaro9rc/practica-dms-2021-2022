""" AnswerServices class module.
"""

from typing import List, Dict, Optional
from sqlalchemy.orm.session import Session  # type: ignore
from dms2122backend.data.config.backendconfiguration import BackendConfiguration
from dms2122backend.data.db.resultsets import answers
from dms2122backend.data.db.schema import Schema
from dms2122backend.data.db.resultsets.answers import Answers
from dms2122backend.data.db.results import Answer

class AnswersServices():
    """ Monostate class that provides high-level services to handle answer-related use cases.
    """

    @staticmethod
    def create_answer(id: int, questionId: int, answer: str, valoration: float, username: str, schema: Schema) -> None:
        """creates an answer given to a question.
        Args:
            - schema (Schema): A database handler where the users are mapped into.            
        Returns:
            -
        """

        session: Session = schema.new_session()
        try:
            Answers.create_answer(session, id, questionId, answer, valoration, username)

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()

    @staticmethod
    def list_all(schema: Schema) -> List[Answer]:
        """Lists all the answers.
        Args:
            - schema (Schema): A database handler where the questions are mapped into.
        Returns:
            - List[Dict]: A list of dictionaries with the questions' data.
        """
        session: Session = schema.new_session()
        answer = Answers.list_all(session)
        schema.remove_session()
        return answer


    @staticmethod
    def list_all_by_user(schema: Schema, user: str) -> List[Answer]:
        """Lists all the answers given by a user.
        Args:
            - schema (Schema): A database handler where the questions are mapped into.
        Returns:
            
        """
        session: Session = schema.new_session()
        answer = Answers.list_all_by_user(session, user)
        schema.remove_session()
        return answer


    @staticmethod
    def list_all_by_question(schema: Schema, questionId: int) -> List[Answer]:
        """Lists all the answers given to a question.
        Args:
            - schema (Schema): A database handler where the questions are mapped into.
        Returns:
            - 
        """
        session: Session = schema.new_session()
        answer = Answers.list_all_by_question(session, questionId)
        schema.remove_session()
        return answer
