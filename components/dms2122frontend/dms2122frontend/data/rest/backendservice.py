""" BackendService class module.
"""

from dms2122common.data import Role
from dms2122common.data.rest import ResponseData
from typing import List, Optional, Dict,  Union
import requests


class BackendService():
    """ REST client to connect to the backend service.
    """

    def __init__(self,
        host: str, port: int,
        api_base_path: str = '/api/v1',
        apikey_header: str = 'X-ApiKey-Backend',
        apikey_secret: str = ''
        ):
        """ Constructor method.

        Initializes the client.

        Args:
            - host (str): The backend service host string.
            - port (int): The backend service port number.
            - api_base_path (str): The base path that is prepended to every request's path.
            - apikey_header (str): Name of the header with the API key that identifies this client.
            - apikey_secret (str): The API key that identifies this client.
        """
        self.__host: str = host
        self.__port: int = port
        self.__api_base_path: str = api_base_path
        self.__apikey_header: str = apikey_header
        self.__apikey_secret: str = apikey_secret

    def __base_url(self) -> str:
        """ Constructs the base URL for the requests.
        Returns:
            - str: The base URL.
        """
        return f'http://{self.__host}:{self.__port}{self.__api_base_path}'



    def create_question(self, token: Optional[str], id: int, questionName: str,
                        description: str, questionAnswer: str, questionAnswer2: str,
                        questionAnswer3: str, correctAnswer: int, puntuation: float, penalty: float) -> ResponseData:
            """ Creates a question.
            Args:
                
            Returns:
                - ResponseData: .
            """
            response_data: ResponseData = ResponseData()
            response: requests.Response = requests.post(
                self.__base_url() + '/question/new',
                json={
                    'id': id,
                    'questionName': questionName,
                    'description': description,
                    'questionAnswer': questionAnswer,
                    'questionAnswer2': questionAnswer2,
                    'questionAnswer3': questionAnswer3,
                    'correctAnswer': correctAnswer,
                    'puntuation': puntuation,
                    'penalty': penalty,
                },
                headers={
                    'Authorization': f'Bearer {token}',
                    self.__apikey_header: self.__apikey_secret
                }
            )
            response_data.set_successful(response.ok)
            if response_data.is_successful():
                response_data.set_content(response.json())
            else:
                response_data.add_message(response.content.decode('ascii'))
            return response_data


    def edit_question(self, token: Optional[str], id: int, questionName: str,
                        description: str, questionAnswer: str, questionAnswer2: str,
                        questionAnswer3: str, correctAnswer: int, puntuation: float, penalty: float) -> ResponseData:
            """ Creates a question.
            Args:
                
            Returns:
                - ResponseData: .
            """
            response_data: ResponseData = ResponseData()
            response: requests.Response = requests.post(
                self.__base_url() + f'/question/{id}',
                json={
                    'id': id,
                    'questionName': questionName,
                    'description': description,
                    'questionAnswer': questionAnswer,
                    'questionAnswer2': questionAnswer2,
                    'questionAnswer3': questionAnswer3,
                    'correctAnswer': correctAnswer,
                    'puntuation': puntuation,
                    'penalty': penalty,
                },
                headers={
                    'Authorization': f'Bearer {token}',
                    self.__apikey_header: self.__apikey_secret
                }
            )
            response_data.set_successful(response.ok)
            if response_data.is_successful():
                response_data.set_content(response.json())
            else:
                response_data.add_message(response.content.decode('ascii'))
            return response_data


    def get_question(self, token: Optional[str], id: int) -> ResponseData:
            """ Requests a question by its id.
            Args:
                token (Optional[str]): The user session token.
                id (int): id of the question
            Returns:
                - ResponseData: .
            """
            response_data: ResponseData = ResponseData()
            response: requests.Response = requests.get(
                self.__base_url() + f'/question/{id}',
                headers={
                    'Authorization': f'Bearer {token}',
                    self.__apikey_header: self.__apikey_secret
                }
            )
            response_data.set_successful(response.ok)
            if response_data.is_successful():
                response_data.set_content(response.json())
            else:
                response_data.add_message(response.content.decode('ascii'))
                response_data.set_content([])
            return response_data

    def list_questions(self, token: Optional[str]) -> ResponseData:
            """ Requests a question by its id.
            Args:
                token (Optional[str]): The user session token.
                id (int): id of the question
            Returns:
                - ResponseData: .
            """
            response_data: ResponseData = ResponseData()
            response: requests.Response = requests.get(
                self.__base_url() + '/question',
                headers={
                    'Authorization': f'Bearer {token}',
                    self.__apikey_header: self.__apikey_secret
                }
            )
            response_data.set_successful(response.ok)
            if response_data.is_successful():
                response_data.set_content(response.json())
            else:
                response_data.add_message(response.content.decode('ascii'))
                response_data.set_content([])
            return response_data


    def get_question_answers(self, token: Optional[str], questionId: int) -> ResponseData:
            """ GEts all the answers of a question
            Args:
                token (Optional[str]): The user session token.
                id (int): id of the question
            Returns:
                - ResponseData: .
            """
            response_data: ResponseData = ResponseData()
            response: requests.Response = requests.get(
                self.__base_url() + f'/answers/{questionId}',
                headers={
                    'Authorization': f'Bearer {token}',
                    self.__apikey_header: self.__apikey_secret
                }
            )
            response_data.set_successful(response.ok)
            if response_data.is_successful():
                response_data.set_content(response.json())
            else:
                response_data.add_message(response.content.decode('ascii'))
                response_data.set_content([])
            return response_data


    def get_student_answers(self, token: Optional[str], username: str) -> ResponseData:
            """ GEts all the answers a user has made
            Args:
                token (Optional[str]): The user session token.
                id (int): id of the question
            Returns:
                - ResponseData: .
            """
            response_data: ResponseData = ResponseData()
            response: requests.Response = requests.get(
                self.__base_url() + f'/answers/{username}',
                headers={
                    'Authorization': f'Bearer {token}',
                    self.__apikey_header: self.__apikey_secret
                }
            )
            response_data.set_successful(response.ok)
            if response_data.is_successful():
                response_data.set_content(response.json())
            else:
                response_data.add_message(response.content.decode('ascii'))
                response_data.set_content([])
            return response_data


    def create_question_answer(self, token: Optional[str], questionId: int, answer: str, valoration: float, username, str) -> ResponseData:
        """ Creates an asnwer.
        Args:
            -
        Returns:
            - ResponseData: If successful, the contents hold the new question's data.
        """
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.post(
            self.__base_url() + f'/question/{questionId}/answer{username}',
            json={
                'questionId': questionId,
                'answer': answer,
                'valoration': valoration,
                'username': username
            },
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret
            }
        )
        response_data.set_successful(response.ok)
        if response_data.is_successful():
            response_data.set_content(response.json())
        else:
            response_data.add_message(response.content.decode('ascii'))
        return response_data