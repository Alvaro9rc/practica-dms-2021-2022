""" StudentEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2122common.data import Role
from dms2122frontend.data.rest import backendservice
from dms2122frontend.data.rest.authservice import AuthService
from dms2122frontend.data.rest.backendservice import BackendService
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
        return render_template('/student/questions.html',  questions=WebQuestion.list_question(backend_service))


    @staticmethod
    def get_student_list_questions(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests to the list of questions names for the student.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))
        return render_template('/student/questions/view.html',  questions=WebQuestion.list_question(backend_service)
                               )
    @staticmethod
    def get_student_list_answer(auth_service: AuthService,  backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests to the list of questions answers for the student.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))
        return render_template('/student/questions/answers.html',  questions=WebQuestion.list_question(backend_service), answers=WebQuestion.list_question_answer(backend_service)
        # return render_template('/student/questions/answers.html',  questions=WebQuestion.list_question(auth_service)
                               )

