""" QuestionServices class module.
"""

from typing import List, Dict, Optional
from sqlalchemy.orm.session import Session  # type: ignore
from dms2122backend.data.db.schema import Schema
from dms2122backend.data.db.resultsets import Questions
from dms2122backend.data.db.results import Question

class QuestionServices():
    """ Class QuestionServices.
    """

    @staticmethod
    def create_question(questionName: str, description: str, questionAnswer: str, questionAnswer2: str, questionAnswer3: str, correctAnswer: int, puntuation: float, penalty: float, schema: Schema) -> Dict:
        """Creates a question.
        Args:
            - schema (Schema): A database handler where the users are mapped into.            

        Returns:
            - 
        """

        session: Session = schema.new_session()
        out: Dict = {}
        try:
            new_question: Question = Questions.create_question(session, questionName, description, questionAnswer, questionAnswer2, questionAnswer3, correctAnswer, puntuation, penalty)
            out['questionName'] = new_question.questionName
        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out


    @staticmethod
    def edit_question(id: int,questionName: str, description: str, questionAnswer: str, questionAnswer2: str, questionAnswer3: str, correctAnswer: int, puntuation: float, penalty: float, schema: Schema) -> Dict:
        """edits a question.
        Args:
            - schema (Schema): A database handler where the users are mapped into.            

        Returns:
            - 
        """
        session: Session = schema.new_session()
        try:
            edited_question: Question = Questions.edit_question(session, id, questionName, description, questionAnswer, questionAnswer2, questionAnswer3, correctAnswer, puntuation, penalty)
        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return edited_question



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
        questions: List[Question] = Questions.list_questions(session)
        for question in questions:
            out.append({
                'questionName': question.questionName,
            })
        schema.remove_session()
        return out