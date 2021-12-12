""" AnswerServices class module.
"""

from typing import List, Dict, Optional
from sqlalchemy.orm.session import Session  # type: ignore
from dms2122backend.data.db.schema import Schema
from dms2122backend.data.db.resultsets.answers import Answers
from dms2122backend.data.db.results import Answer

class AnswersServices():
    """ Monostate class that provides high-level services to handle answer-related use cases.
    """

    @staticmethod
    def create_question_answer(questionId: int, answer: str, valoration: float, username: str, schema: Schema) -> None:
        """creates an answer given to a question.
        Args:
            - schema (Schema): A database handler where the users are mapped into.            
        Returns:
            -
        """

        session: Session = schema.new_session()
        try:
            Answers.create_question_answer(session, questionId, answer, valoration, username)

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()


    @staticmethod
    def get_student_answers( username: str, schema: Schema) -> List[Answer]:
        """Lists all the answers given by a user.
        Args:
            - schema (Schema): A database handler where the questions are mapped into.
        Returns:
            
        """
        session: Session = schema.new_session()
        answer = Answers.get_student_answers(session, username)
        schema.remove_session()
        return answer


    @staticmethod
    def get_question_answers(id: int, schema: Schema) -> List[Answer]:
        """Lists all the answers given to a question.
        Args:
            - schema (Schema): A database handler where the questions are mapped into.
        Returns:
            - 
        """
        session: Session = schema.new_session()
        answer = Answers.get_question_answers(session, id)
        schema.remove_session()
        return answer
