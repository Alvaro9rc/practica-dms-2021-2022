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

        response: ResponseData = auth_service.list_users(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def create_question(auth_service: AuthService, questionName: str, description:str, questionAnswer:str, IncorrectAnswer:str, IncorrectAnswer2:str, puntuacion, porcentaje) -> Optional[Dict]:
        question = {}
        # question['question'] =  questionName
        # question['description'] =  description
        # question['questionAnswer'] =  questionAnswer
        # question['incorrectAnswer'] =  IncorrectAnswer
        # question['incorrectAnswer2'] =  IncorrectAnswer2
        # question['puntuacion'] =  puntuacion
        # question['porcentaje'] =  porcentaje
        # TODO METER EN UN DICCIONARIO Y DEVOLVERLO
        return question
    

