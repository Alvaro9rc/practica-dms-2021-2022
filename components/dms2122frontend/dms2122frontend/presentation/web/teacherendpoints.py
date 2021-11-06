""" TeacherEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2122common.data import Role
from dms2122frontend.data.rest.authservice import AuthService
from flask import redirect, url_for, session, render_template, request, flash

from dms2122frontend.presentation.web.webquestion import WebQuestion
from .webauth import WebAuth


class TeacherEndpoints():
    """ Monostate class responsible of handing the teacher web endpoint requests.
    """
    @staticmethod
    def get_teacher(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the teacher root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        return render_template('teacher.html', name=name, roles=session['roles'])

    @staticmethod
    def get_teacher_questions(auth_service: AuthService) -> Union[Response, Text]:
        name = session['user']
        return render_template('teacher/questions.html')

    @staticmethod
    def get_teacher_questions_new(auth_service: AuthService) -> Union[Response, Text]:
        name = session['user']
        redirect_to = request.args.get(
            'redirect_to', default='/teacher/questions')
        return render_template('teacher/questions/new.html', name=name, roles=session['roles'],
                               redirect_to=redirect_to
                               )

    @staticmethod
    def post_teacher_questions_new(auth_service: AuthService) -> Union[Response, Text]:

        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        created_question = WebQuestion.create_question(auth_service,
                                                       request.form['questionName'], request.form['description'], request.form[
                                                           'questionAnswer'], request.form["IncorrectAnswer"], request.form["IncorrectAnswer2"],request.form["puntuacion"], request.form["porcentaje"]
                                                       )
        if not created_question:
            return redirect(url_for('get_teacher_questions_new'))
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            redirect_to = url_for('get_teacher_questions')
        return redirect(redirect_to)
