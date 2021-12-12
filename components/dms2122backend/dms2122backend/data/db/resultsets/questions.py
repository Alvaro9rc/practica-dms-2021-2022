""" Questions class module.
"""

import hashlib
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2122backend.data.db.results import Question
from dms2122backend.data.db.exc.questionexisterror import QuestionExistsError
from dms2122backend.data.db.exc.questionnotfounderror import QuestionNotFoundError

class Questions():
    """ Class Question. (no utilizada en esta entrega)
    """
    # @staticmethod
    # def list_all(session: Session) -> List[Dict]:
    # # def list_all(session: Session) -> List[Question]:
    #     """ Gets the list of questions from the database.

    #     Args:
    #         - session (Session): The session object.

    #     Returns:
    #         - List: A list object with the questions.
    #     """
    #     # query = session.query(Question)
    #     # return query.all()
    #     out: List[Dict] = []
    #     out.append(
    #         {
    #             'id': 1,
    #             'questionName': "¿Quién Inventó la luz?",
    #             'description': "Esto es una pregunta",
    #             'questionAnswer': "La luz ya existía",
    #             'questionAnswer2': "Alberto Porres",
    #             'questionAnswer3': "Guttemberg",
    #             'puntuation': 20,
    #             'penalty':10,
    #             'userCreated': 1


    #         })
    #     out.append({
    #             'id': 2,
    #             'questionName': "¿Cuántas Patas tiene un caballo?",
    #             'description': "Pregunta fácil para aprobar",
    #             'questionAnswer': "Tiene cola",
    #             'questionAnswer2': "Tiene 4 patas",
    #             'questionAnswer3': "No existen los caballos",
    #             'puntuation': 10,
    #             'penalty': 5,
    #             'userCreated': 1

    #         })
    #     out.append({
    #             'id': 3,
    #             'questionName': "Cuál es el radio de la tierra? en km",
    #             'description': "Pregunta fácil para aprobar",
    #             'questionAnswer': "6700 km",
    #             'questionAnswer2': "8000 km",
    #             'questionAnswer3': "7700 km",
    #             'puntuation': 10,
    #             'penalty': 20,
    #             'userCreated': 1

    #         })
    #     return out

    @staticmethod
    def create_question(session: Session,  questionName: str, description: str, questionAnswer: str, questionAnswer2: str, questionAnswer3: str, correctAnswer: int, puntuation: float, penalty: float) -> Question:
        """ Creates a new question.
        Note:
            Any existing transaction will be committed.
        Args:
            - session (Session): The session object.
            - 
        Raises:
            - ValueError: If any field is empty.
            - QuestionExistsError: If a question with the same title already exists.
        Returns:
            - Question: The created Question.
        """
        if not questionName or not description or not questionAnswer or not questionAnswer2 or not questionAnswer3 or not correctAnswer or not puntuation or not penalty:
            raise ValueError('All fields are required.')
        try:
            new_question = Question(questionName, description, questionAnswer, questionAnswer2, questionAnswer3, correctAnswer, puntuation, penalty)
            session.add(new_question)
            session.commit()
            return new_question
        except IntegrityError as ex:
            raise QuestionExistsError(
                'A question named ' + questionName + ' already exists.'
                ) from ex
        
    @staticmethod
    def edit_question(session: Session, id: int,questionName: str, description: str, questionAnswer: str, questionAnswer2: str, questionAnswer3: str, correctAnswer: int, puntuation: float, penalty: float) -> Question:
        """ edits a question question.
        Note:
            Any existing transaction will be committed.
        Args:
            - session (Session): The session object.
            - 
        Raises:
            - ValueError: If any field is empty.
            - QuestionExistsError: If a question with the same title already exists.
        Returns:
            - Question: The created Question.
        """
        question = Questions.get_question(session, id)
        if question is None:
            raise QuestionNotFoundError
        else:
            question.questionName = questionName
            question.description = description
            question.questionAnswer = questionAnswer
            question.questionAnswer2 = questionAnswer2
            question.questionAnswer3 = questionAnswer3
            question.correctAnswer = correctAnswer
            question.puntuation = puntuation
            question.penalty = penalty

            session.commit()
            return question


    @staticmethod
    def get_question(session: Session, id: int) -> Optional[Question]:
        """ Gets a question by its id.
        Args:
            - id: (int): Question id.
        Returns:
            - bool: True if the question exist and false if not.
        """
        try:
            query = session.query(Question).filter_by(id = id)
            question: Question = query.one()
        except NoResultFound:
            return None
        return question
    

    @staticmethod
    def list_questions(session: Session) -> List[Question]:
        """Lists all the question.
        Args:
            - session (Session): The session object.
        Returns:
            - List[Question]: A list of all the questions.
        """
        query = session.query(Question)
        return query.all()

    

    # @staticmethod
    # def get_question_by_name(session: Session, name: str) -> Optional[Question]:
    #     """ Gets a question by its name.
    #     Args:
    #         - name: (str): Question name.
    #     Returns:
    #         - bool: True if the question exist and false if not.
    #     """
    #     try:
    #         query = session.query(Question).filter_by(name = name)
    #         question: Question = query.one()
    #     except NoResultFound:
    #         return None
    #     return question
