""" QuestionServices class module.
"""

from typing import List, Dict, Optional
from sqlalchemy.orm.session import Session  # type: ignore
from dms2122backend.data.db.schema import Schema
from dms2122backend.data.db.resultsets.questions import Questions
from dms2122backend.data.db.results.question import Question

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
            out['id'] = new_question.id
            out['questionName'] = new_question.questionName
            out['description'] = new_question.description
            out['questionAnswer'] = new_question.questionAnswer
            out['questionAnswer2'] = new_question.questionAnswer2
            out['questionAnswer3'] = new_question.questionAnswer3
            out['correctAnswer'] = new_question.correctAnswer
            out['puntuation'] = new_question.puntuation
            out['penalty'] = new_question.penalty
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
        out: Dict = {}
        try:
            edited_question: Question = Questions.edit_question(session, id, questionName, description, questionAnswer, questionAnswer2, questionAnswer3, correctAnswer, puntuation, penalty)
            out['id'] = edited_question.id
            out['questionName'] = edited_question.questionName
            out['description'] = edited_question.description
            out['questionAnswer'] = edited_question.questionAnswer
            out['questionAnswer2'] = edited_question.questionAnswer2
            out['questionAnswer3'] = edited_question.questionAnswer3
            out['correctAnswer'] = edited_question.correctAnswer
            out['puntuation'] = edited_question.puntuation
            out['penalty'] = edited_question.penalty
        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out



    @staticmethod
    def get_question( id: int, schema: Schema)-> Dict:
        """ Requests the question from the database by its id.
        Args:
            - schema (Schema): A database handler where the users are mapped into.
            
        Returns:
            - Question: the question found.
        """        
        session: Session = schema.new_session()
        out: Dict = {}
        question = Questions.get_question(session, id)
        out['id'] = question.id
        out['questionName'] = question.questionName
        out['description'] = question.description
        out['questionAnswer'] = question.questionAnswer
        out['questionAnswer2'] = question.questionAnswer2
        out['questionAnswer3'] = question.questionAnswer3
        out['correctAnswer'] = question.correctAnswer
        out['puntuation'] = question.puntuation
        out['penalty'] = question.penalty
        schema.remove_session()
        return out


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
                'id': question.id,
                'questionName': question.questionName,
                'description': question.description,
                'questionAnswer': question.questionAnswer,
                'questionAnswer2': question.questionAnswer2,
                'questionAnswer3': question.questionAnswer3,
                'correctAnswer': question.correctAnswer,
                'puntuation': question.puntuation,
                'penalty': question.penalty
            })
        schema.remove_session()
        return out