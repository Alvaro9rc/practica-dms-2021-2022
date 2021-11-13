""" Webquestion class module.
"""

from typing import Dict, List, Optional
from flask import session
from dms2122common.data.rest import ResponseData
from dms2122frontend.data.rest.authservice import AuthService
from .webutils import WebUtils


class WebQuestion():
    """ Monostate class responsible of the queston operation utilities.
    """
    @staticmethod
    def list_question(auth_service: AuthService) -> List:

        response: ResponseData = auth_service.list_questions(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []
    @staticmethod
    def list_question_answer(auth_service: AuthService) -> List:

        response: ResponseData = auth_service.list_questions_answer(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

# TODO pendiente por hacer en AUTSERVICES
    @staticmethod
    def create_question(auth_service: AuthService, questionName: str, description:str, questionAnswer:str, questionAnswer2:str, questionAnswer3:str, puntuation:str, penalty:str) -> Optional[Dict]:
        response: ResponseData = auth_service.create_teacher_question(
            session.get('token'), questionName, description, questionAnswer, questionAnswer2, questionAnswer3, puntuation, penalty)
        WebUtils.flash_response_messages(response)
        return response.get_content()
    

    @staticmethod
    def update_teacher_question(auth_service: AuthService,  id:str, questionName:str, description:str, questionAnswer:str, questionAnswer2:str, questionAnswer3:str, puntuation:str, penalty:str) -> bool:

        response: ResponseData = auth_service.update_teacher_question(
            session.get('token'), id, questionName, description, questionAnswer, questionAnswer2, questionAnswer3, puntuation, penalty)
        WebUtils.flash_response_messages(response)
        return response.is_successful()
