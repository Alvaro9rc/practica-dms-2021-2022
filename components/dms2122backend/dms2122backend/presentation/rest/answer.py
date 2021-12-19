""" REST API controllers responsible of handling the user operations.
"""

from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app
from dms2122backend.service.answerservices import AnswersServices
# from dms2122auth.service import RoleServices
# from dms2122common.data.role import Role
from dms2122backend.data.db.exc.questionnotfounderror import QuestionNotFoundError


def create_question_answer(body: Dict, token_info: Dict) -> Tuple[Optional[str], Optional[int]]:
    """ creates a question if the user has the teacher role.
    """
    with current_app.app_context():
        # if not RoleServices.has_role(token_info['user_token']['user'], Role.Student, current_app.db):
        #     return (
        #         'Current user has not enough privileges to answer a question',
        #         HTTPStatus.FORBIDDEN.value
        #     )
        try:
             AnswersServices.create_answer(body['questionId'],
             body['answer'], body['valoration'], body['username'], current_app.db)
                

        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
        except QuestionNotFoundError:
            return ('The question does not exist', HTTPStatus.CONFLICT.value)
    return (None, HTTPStatus.OK.value)


def get_student_answers(username: str, token_info: Dict) -> Tuple[Union[List[Dict], str], Optional[int]]:
    """ 
    """
    with current_app.app_context():
        # if not RoleServices.has_role(token_info['user_token']['user'], Role.Student, current_app.db):
        #     return (
        #         'Current user has not enough privileges to view his answers',
        #         HTTPStatus.FORBIDDEN.value
        #     )
        try:
            answers: List[Dict] = AnswersServices.get_student_answers(
                username, current_app.db
            )
        except ValueError:
            return ("A mandatory argument is missing", HTTPStatus.BAD_REQUEST.value)
        return (answers, HTTPStatus.OK.value)




def get_question_answers(id: int, token_info: Dict) -> Tuple[Union[List[Dict], str], Optional[int]]:
    """ 
    """
    with current_app.app_context():
        # if not RoleServices.has_role(token_info['user_token']['user'], Role.Teacher, current_app.db):
        #     return (
        #         'Current user has not enough privileges to view question answers',
        #         HTTPStatus.FORBIDDEN.value
        #     )
        try:
            answers: List[Dict] = AnswersServices.get_question_answers(
                id, current_app.db
            )
        except ValueError:
            return ("A mandatory argument is missing", HTTPStatus.BAD_REQUEST.value)
        return (answers, HTTPStatus.OK.value)





