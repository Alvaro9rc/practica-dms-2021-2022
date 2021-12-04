""" REST API controllers responsible of handling the user operations.
"""

from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app
from dms2122backend.data.db.results.answer import Answer
from dms2122backend.service.answerservices import AnswersServices
from dms2122auth.service import RoleServices
from dms2122common.data.role import Role
from dms2122backend.data.db.exc.questionnotfounderror import QuestionNotFoundError


def create_answer(body: Dict, token_info: Dict) -> Tuple[Optional[str], Optional[int]]:
    """ creates a question if the user has the teacher role.
    """
    with current_app.app_context():
        if not RoleServices.has_role(token_info['user_token']['user'], Role.Student, current_app.db):
            return (
                'Current user has not enough privileges to answer a question',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            answer: Dict = AnswersServices.create_answer(body['id'], body['questionId'],
             body['answer'], body['valoration'], body['username'], current_app.db)
                

            
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
        except QuestionNotFoundError:
            return ('The question does not exist', HTTPStatus.CONFLICT.value)
    return (answer, HTTPStatus.OK.value)



def list_all() -> Tuple[List[Dict], Optional[int]]:
    """ 
    """
    with current_app.app_context():
        Answer: List[Dict] = AnswersServices.list_all(current_app.db)
    return (Answer, HTTPStatus.OK.value)



def list_all_by_user(user: str) -> Tuple[List[Dict], Optional[int]]:
    """ 
    """
    with current_app.app_context():
        Answer: List[Dict] = AnswersServices.list_all_by_user(user, current_app.db)
    return (Answer, HTTPStatus.OK.value)

def list_all_by_question(questionId: int) -> Tuple[List[Dict], Optional[int]]:
    """ 
    """
    with current_app.app_context():
        Answer: List[Dict] = AnswersServices.list_all_by_question(questionId ,current_app.db)
    return (Answer, HTTPStatus.OK.value)