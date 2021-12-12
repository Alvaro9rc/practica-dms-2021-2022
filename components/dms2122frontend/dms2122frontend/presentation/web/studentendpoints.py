""" StudentEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template, request
from werkzeug.wrappers import Response
from dms2122common.data import Role
from dms2122frontend.data.rest import BackendService
from dms2122frontend.data.rest.authservice import AuthService
from dms2122frontend.data.rest.backendservice import BackendService
from dms2122frontend.presentation.web.webanswer import WebAnswer
from dms2122frontend.presentation.web.webquestion import WebQuestion
from typing import  Dict, List
from .webauth import WebAuth


class StudentEndpoints():
    """ Monostate class responsible of handling the student web endpoint requests.
    """
    @staticmethod
    def get_student(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the student root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        return render_template('student.html', name=name, roles=session['roles'])

    @staticmethod
    def get_student_questions(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests to the questions for the student.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']


        # TODO coger solo las preguntas que no tienen respuesta 
        return render_template('/student/questions.html', name=name, roles=session['roles'],  questions=WebQuestion.list_question(backend_service))


    @staticmethod
    def get_student_questions_question(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests to a specific question.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        # id de la pregunta
        id: int = int(request.args.get('id'))
        redirect_to: str = str(request.args.get(
            'redirect_to', default='/student/questions'))
        name = session['user']

        # en el .html se tiene que hacer el formulario
        return render_template('/student/questions/question.html', name=name, roles=session['roles'], questions=WebQuestion.get_question(backend_service, id), redirect_to = redirect_to)



    @staticmethod
    def post_student_questions_question(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the POST requests to answer a question.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))
        
        #HAY QUE CAMBIAR LA CLASE ANSWER YA QUE LA GESTION DE LAS IDS ES MUY COMPLEJA

        #TODO GESTION DE LA PUNTUACION OPTENIDA.
        value = 0
        name = session['user']
        successful: bool = True
 
        successful &= WebAnswer.create_question_answer(backend_service,
                                                request.form['id'],
                                                request.form['answer'],
                                                value,
                                                name                                               
                                                )
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            redirect_to = url_for('get_teacher_questions')
        return redirect(redirect_to)


    @staticmethod
    def get_student_answers(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests to the answers the student has made.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']

        return render_template('/student/answers.html', name=name, roles=session['roles'],  answers=WebAnswer.get_student_answers(backend_service, name))



    @staticmethod
    def get_student_progress(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests to the answers the student has made.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        #TODO PROGRESO DEL ALUMNO