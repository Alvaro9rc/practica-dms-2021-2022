""" REST API controllers responsible of handling the user operations.
"""

from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app
from dms2122backend.data.db.results.question import Question
from dms2122backend.service.questionservices import QuestionServices
from dms2122auth.service import RoleServices
from dms2122common.data.role import Role
from dms2122backend.data.db.exc.questionexisterror import QuestionExistsError


def create_question(body: Dict, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    """ creates a question if the user has the teacher role.
    """
    with current_app.app_context():
        if not RoleServices.has_role(token_info['user_token']['user'], Role.Teacher, current_app.db):
            return (
                'Current user has not enough privileges to create a question',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            question: Dict = QuestionServices.create_question( body['questionName'],
             body['description'], body['questionAnswer'], body['questionAnswer2'], body['questionAnswer3'], 
             body['correctAnswer'], body['puntuation'], body['penalty'], current_app.db)
            
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
        except QuestionExistsError:
            return ('A question like this already exists', HTTPStatus.CONFLICT.value)
    return (question, HTTPStatus.OK.value)


def edit_question(body: Dict, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    """ edit a question if the user has the teacher role.
    """
    

def get_question(id: int) -> Tuple[Union[Optional[Question], str], Optional[int]]:
    """get question.
    """
    try:
        question = QuestionServices.get_question(
            id, current_app.db
        )
    except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (question, HTTPStatus.OK.value)



def list_questions() -> Tuple[List[Dict], Optional[int]]:
    """ Gets the list of question dictionaries.

        Returns:
            - Tuple: Question dictionaries.
            - Optional: boolean 1 or 0 in case the petition was succesfull.
        """
    with current_app.app_context():
        questions: List[Dict] = QuestionServices.list_questions(current_app.db)
    return (questions, HTTPStatus.OK.value)

 