""" QuestionServices class module.
"""

from typing import List, Dict, Optional
from sqlalchemy.orm.session import Session  # type: ignore
from dms2122backend.data.config.backendconfiguration import BackendConfiguration
from dms2122backend.data.db.schema import Schema
from dms2122backend.data.db.resultsets import Questions
from dms2122backend.data.db.results import Question

class QuestionServices():
    """ Class QuestionServices.
    """

    @staticmethod
    def create_question(id: int,  questionName: str, description: str, questionAnswer: str, questionAnswer2: str, questionAnswer3: str, correctAnswer: str, puntuation: int, penalty: int, schema: Schema) -> None:
        """Creates a question.
        Args:
            - schema (Schema): A database handler where the users are mapped into.            

        Returns:
            - 
        """

        session: Session = schema.new_session()
        try:
            new_question: Question = Questions.create_question(session, id, questionName, description, questionAnswer, questionAnswer2, questionAnswer3, correctAnswer, puntuation, penalty)
        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()

    @staticmethod
    def get_question( id: int, schema: Schema)-> Optional[Question]:
        """ Requests the question from the database by its id.
        Args:
            - schema (Schema): A database handler where the users are mapped into.
            
        Returns:
            - Question: the question found.
        """        
        
        session: Session = schema.new_session()
        question = Questions.get_question(session, id)
        schema.remove_session()
        return question

    @staticmethod
    def get_question_by_name( name: str, schema: Schema)-> Optional[Question]:
        """ Requests the question from the database by its name.
        Args:
            - schema (Schema): A database handler where the users are mapped into.
            
        Returns:
            - Question: the question found.
        """        
        
        session: Session = schema.new_session()
        question = Questions.get_question_by_name(session, name)
        schema.remove_session()
        return question

    @staticmethod
    def list_questions(schema: Schema) -> List[Dict]:
        """ Requests the questions from the database into a list of dictionaries 
            for the frontend.

        Args:
            - schema (Schema): A database handler where the users are mapped into.

        Returns:
            - List: A list object with the dictionaries.
        """
        out: List[Dict] = []
        session: Session = schema.new_session()
        questions: List[Question] = Questions.list_all(session)
        for question in questions:
            out.append({
                'id': question.id,
                'questionName': question.questionName,
                'description': question.description,
                'questionAnswer': question.questionAnswer,
                'questionAnswer2': question.questionAnswer2,
                'questionAnswer3': question.questionAnswer3,
                'correctAnswer': question.correctAnswer,
                'puntuation': question.puntuation,
                'penalty': question.penalty, 

            })
        schema.remove_session()
        return out