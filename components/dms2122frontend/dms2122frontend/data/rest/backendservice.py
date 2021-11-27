""" BackendService class module.
"""
# from dms2122backend.data.db.orm.results import Role
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
        return f'http://{self.__host}:{self.__port}{self.__api_base_path}'

    # TODO: Implement


    def update_teacher_question(self,
                          token: Optional[str], id:int, questionName: str,description: str,questionAnswer: str,questionAnswer2: str,questionAnswer3: str,puntuation: int,penalty: int, userCreated:str
                          ) -> ResponseData:
        aggregated_response: ResponseData = ResponseData()
        aggregated_response.set_successful(True)
        """ Requests to update several questions for the teacher.

        This utility method is not completely developed because the questions capability of been 
        updated isn't supose to be working yet.

        Args:
            - token (Optional[str]): The user session token.
            - id (int): Id of the question to be updated.
            - questionName (str): New posible name.
            - description (str): New posible description.
            - questionAnswer (str): New posible first answer.
            - questionAnswer2 (str): New posible second answer.
            - questionAnswer3 (str): New posible  third answer.
            - puntuation (int): New posible puntuation.
            - penalty (int): New posible penalty.

        Returns:
            - ResponseData: Useful to know whether the operation succeeded and its messages.
        """

# TODO PENDIENTE DE CREAR LA FUNCION PARA GUARDAR LOS DATOS DE ESTA QUESTION EN CONCRETO va a fallar mientras el guardado en el back no funcione
    # Esta función llamará al set_question_data para asignar las nuevas opciones a la cuestion
        # response = self.set_question_data(token, id, questionName, description, questionAnswer, questionAnswer2, questionAnswer3, puntuacion, penalty)

        # aggregated_response.add_messages(response.get_messages())
        # aggregated_response.set_successful(
        #     aggregated_response.is_successful() & response.is_successful())
        return aggregated_response


# TODO pendiente de desarrollar esta funcion para crear una pregunta nueva
    def create_teacher_question(self,
                          token: Optional[str], questionName: str,description: str,questionAnswer: str,questionAnswer2: str,questionAnswer3: str,puntuation: int, penalty: int, userCreated: str
                          ) -> ResponseData:
        """ Requests to create a question for the teacher.

        This utility method is not completely developed because the questions capability of having 
        new questions added isn't supose to be working yet.

        Args:
            - token (Optional[str]): The user session token.
            - questionName (str): Question name.
            - description (str): Question description.
            - questionAnswer (str): Question first answer.
            - questionAnswer2 (str): Question second answer.
            - questionAnswer3 (str): Question  third answer.
            - puntuation (str): Question puntuation.
            - penalty (str): Question penalty.

        Returns:
            - ResponseData: Useful to know whether the operation succeeded and its messages.
        """

        aggregated_response: ResponseData = ResponseData()
        # Para esta entregan le damos el valor True para que no de errores en ejecucion
        aggregated_response.set_successful(True)
        
        # IMPORTANTE PARA LA PARTE DEL BACK, SE ENVIAN LAS OPCIONES DEL FORMULARIO EN UN JSON PARA GUARDARLAS POSTERIORMENTE 
        # TODO para cuando se envie al back yhay que definir la ruta /question/new en/  en (spec.yml)
        # response: requests.Response = requests.post(
        #     self.__base_url() + 'question/new',
        #     json={
        #         'questionName': questionName,
        #         'description': description,
        #         'questionAnswer': questionAnswer,
        #         'questionAnswer2': questionAnswer2,
        #         'questionAnswer3': questionAnswer3,
        #         'puntuation': puntuation,
        #         'penalty': penalty
        #     },
        #     headers={
        #         'Authorization': f'Bearer {token}',
        #         self.__apikey_header: self.__apikey_secret
        #     }
        # )
        # aggregated_response.set_successful(response.ok)
        # if aggregated_response.is_successful():
        #     aggregated_response.set_content(response.json())
        # else:
        #     aggregated_response.add_message(response.content.decode('ascii'))
        return aggregated_response

    def list_questions(self, token: Optional[str]) -> ResponseData:
        """ Requests the question list from the database.

        ** No hemos conseguido obtener las cuestiones mediante una ruta para realizar una 
        consulta a la base de datos, la ruta se debería desarrollar en el fichero .yml 
        (esta comentada). Puesto que nos daba un error en el login hemos insertado manualmente
        las cuestiones aquí. Puesto que está la funcionalidad para obtener las cuestiones desde la
        'base de datos' una vez corregido el error de la ruta se reemplazará este fragmento de código
        por el del comentario situado debajo.

        Args:
            - token (Optional[str]): The user session token.
        Returns:
            - ResponseData: Useful to know whether the operation succeeded and its messages.
        """

        response_data: ResponseData = ResponseData()
        # response_data.set_successful(True)
        # out: List[Dict] = []
        # out.append(
        #     {
        #         'id': 1,
        #         'questionName': "¿Quién Inventó la luz?",
        #         'description': "Esto es una pregunta",
        #         'questionAnswer': "La luz ya existía",
        #         'questionAnswer2': "Alberto Porres",
        #         'questionAnswer3': "Guttemberg",
        #         'puntuation': 20,
        #         'penalty':10,
        #         'userCreated': 1


        #     })
        # out.append({
        #         'id': 2,
        #         'questionName': "¿Cuántas Patas tiene un caballo?",
        #         'description': "Pregunta fácil para aprobar",
        #         'questionAnswer': "Tiene cola",
        #         'questionAnswer2': "Tiene 4 patas",
        #         'questionAnswer3': "No existen los caballos",
        #         'puntuation': 10,
        #         'penalty': 5,
        #         'userCreated': 1

        #     })
        # out.append({
        #         'id': 3,
        #         'questionName': "Cuál es el radio de la tierra? en km",
        #         'description': "Pregunta fácil para aprobar",
        #         'questionAnswer': "6700 km",
        #         'questionAnswer2': "8000 km",
        #         'questionAnswer3': "7700 km",
        #         'puntuation': 10,
        #         'penalty': 20,
        #         'userCreated': 1

        #     })
        # response_data.set_content(out)
        response: requests.Response = requests.get(
            self.__base_url() + '/questions',
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

    def list_questions_answer(self, token: Optional[str]) -> ResponseData:
        """ Requests the list of answers of the answered questions  from the database.

        Args:
            - token (Optional[str]): The user session token.
        Returns:
            - ResponseData: Useful to know whether the operation succeeded and its messages.
        """

        response_data: ResponseData = ResponseData()
        response_data.set_successful(True)
        out: List[Dict] = []
        out.append(
            {
                'id': 1,
                'questionId': 1,
                'answer': 2,
                'puntuation': "-20",
                'username': 'Usuario1'

            })
        out.append({
                'id': 2,
                'questionId': 2,
                'answer': 2,
                'puntuation': "-20",
                'username': 'Usuario1'
            })
        response_data.set_content(out)
        return response_data
