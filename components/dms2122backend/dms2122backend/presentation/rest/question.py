""" REST API controllers responsible of handling the user operations.
"""

from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app
from dms2122backend.data.db.results.question import Question
from dms2122backend.service.questionservices import QuestionServices
from dms2122common.data.role import Role
from dms2122auth.service import RoleServices
from dms2122backend.data.db.exc.questionexisterror import QuestionExistsError
from dms2122backend.data.db.exc.questionnotfounderror import QuestionNotFoundError

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


def edit_question(id: int, body: Dict, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    """ edit a question if the user has the teacher role.
    """
    with current_app.app_context():
        if not RoleServices.has_role(token_info['user_token']['user'], Role.Teacher, current_app.db):
            return (
                'Current user has not enough privileges to edit a question',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            edited_question: Dict = QuestionServices.edit_question(id, body['questionName'],
             body['description'], body['questionAnswer'], body['questionAnswer2'], body['questionAnswer3'], 
             body['correctAnswer'], body['puntuation'], body['penalty'], current_app.db)
            
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
        except QuestionNotFoundError:
            return ('A question with this id doesnt exists', HTTPStatus.CONFLICT.value)
    return (edited_question, HTTPStatus.OK.value)
    

def get_question(id: int) -> Tuple[Union[Dict, str], Optional[int]]:
    """get question.
    """    
    with current_app.app_context():
        try:
            question: Dict = QuestionServices.get_question(
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
