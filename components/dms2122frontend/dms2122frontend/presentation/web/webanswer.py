""" WebAnswer class module.
"""

from typing import Dict, List, Optional
from flask import session
from dms2122common.data.rest import ResponseData
from dms2122frontend.data.rest.backendservice import BackendService
from .webutils import WebUtils

class WebAnswer():
    """ Monostate class responsible of the question operation utilities.
    """

    @staticmethod
    def get_question_answers(backend_service: BackendService,  id:int) -> List:
        """ gets all the answers to a question.

        Args:
            - auth_service (AuthService): The authentication service.
            - id (str): Question Id.

        Returns:
            - Bool: true if the request is successful.
        """
        response: ResponseData = backend_service.get_question_answers(
            session.get('token'), id)
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def get_student_answers(backend_service: BackendService,  username:str) -> List:
        """ get all the answers a studen has given.

        Args:
            - auth_service (AuthService): The authentication service.
            - id (str): Question Id.

        Returns:
            - Bool: true if the request is successful.
        """
        response: ResponseData = backend_service.get_student_answers(
            session.get('token'), username)
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []


    @staticmethod
    def create_question_answer(backend_service: BackendService, questionId: int, answer: str, valoration: float, username, str) -> Optional[Dict]:
        """ create answer.

        Args:
            - auth_service (AuthService): The authentication service.
            - id (str): Question Id.

        Returns:
            - Bool: true if the request is successful.
        """
        response: ResponseData = backend_service.create_question_answer(
            session.get('token'),questionId, answer, valoration, username)
        WebUtils.flash_response_messages(response)
        return response.get_content()
