""" Webquestion class module.
"""

from typing import Dict, List, Optional
from flask import session
from dms2122common.data.rest import ResponseData
from dms2122frontend.data.rest.authservice import AuthService
from dms2122frontend.data.rest.backendservice import BackendService
from .webutils import WebUtils


class WebQuestion():
    """ Monostate class responsible of the queston operation utilities.
    """
    @staticmethod
    def list_question(backend_service: BackendService) -> List:
        """ Gets the list of questions-

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - List: The list of questions.
        """
        response: ResponseData =backend_service.list_questions(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def list_question_answer( backend_service:BackendService) -> List:
        """ Gets the list of question answers.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - List: The list of answers.
        """
        response: ResponseData = backend_service.list_questions_answer(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    # TODO pendiente por hacer en AUTSERVICES
    @staticmethod
    def create_question( backend_service: BackendService, questionName: str, description:str, questionAnswer:str, questionAnswer2:str, questionAnswer3:str, puntuation:int, penalty:int, userCreated:str) -> Optional[Dict]:
        """ Creates the new question requested by the teacher.

        Args:
            - auth_service (AuthService): The authentication service.
            - questionName (srt): Question name.
            - description (srt): Description of the question.
            - questionAnswer (srt): First answer.
            - questionAnswer2 (srt): Second answer.
            - questionAnswer3 (srt): Third answer.
            - puntuation (srt): Puntuacion of the question.
            - penalty (srt): Penalty of the question.

        Returns:
            - Optional: true if the request is successful.
        """
        response: ResponseData = backend_service.create_teacher_question(
            session.get('token'), questionName, description, questionAnswer, questionAnswer2, questionAnswer3, puntuation, penalty, userCreated)
        
        WebUtils.flash_response_messages(response)
        return response.get_content()
    

    @staticmethod
    def update_teacher_question(backend_service: BackendService,  id:int, questionName:str, description:str, questionAnswer:str, questionAnswer2:str, questionAnswer3:str, puntuation:int, penalty:int, userCreated:str) -> bool:
        """ Updates a question requested by the teacher.

        Args:
            - auth_service (AuthService): The authentication service.
            - id (str): Question posible new Id.
            - questionName (srt): Question posible new name.
            - description (srt): posible new description of the question.
            - questionAnswer (srt): posible new first answer.
            - questionAnswer2 (srt): posible new second answer.
            - questionAnswer3 (srt): posible new third answer.
            - puntuation (srt): posible new puntuacion.
            - penalty (srt): posible new penalty.

        Returns:
            - Bool: true if the request is successful.
        """
        response: ResponseData = backend_service.update_teacher_question(
            session.get('token'), id, questionName, description, questionAnswer, questionAnswer2, questionAnswer3, puntuation, penalty)
        WebUtils.flash_response_messages(response)
        return response.is_successful()
