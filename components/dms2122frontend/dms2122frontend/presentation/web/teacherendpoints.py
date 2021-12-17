""" TeacherEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2122common.data import Role
from dms2122frontend.data.rest.authservice import AuthService
from flask import redirect, url_for, session, render_template, request, flash
from dms2122frontend.data.rest.backendservice import BackendService
from dms2122frontend.presentation.web.webanswer import WebAnswer
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
    def get_teacher_questions(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests for the teacher questions.
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
        
        questions=WebQuestion.list_question(backend_service)
        answered = []
        unanswered = []
        
        for question in questions:
            #si la pregunta tiene una o mas respuestas ha sido contestada
            if (len(WebAnswer.get_question_answers(backend_service, int(question['id']))) > 0):
                answered.append(question)
            else:
                unanswered.append(question)
            
        return render_template('teacher/questions.html', name=name, roles=session['roles'], answered = answered, unanswered = unanswered)

    @staticmethod
    def get_teacher_questions_new(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests for a new question created by the teacher.
        Args:
            - auth_service (AuthService): The authentication service.
        Returns:
            - Union[Response,Text]: The generated response to the request.
        """

        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Admin.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        redirect_to = request.args.get('redirect_to', default='/teacher/questions')
        return render_template('admin/users/new.html', name=name, roles=session['roles'],
                               redirect_to=redirect_to
                               )



    @staticmethod
    def post_teacher_questions_new(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the POST for a new question created by the teacher.
        Args:
            - auth_service (AuthService): The authentication service.
        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        '''Endpoint para el creado de preguntas '''

        #Controlamos que el usuario se haya logeado
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))
        if (request.form['questionAnswer'] == request.form['questionAnswer2']) or (request.form['questionAnswer'] == request.form['questionAnswer3']) or (request.form['questionAnswer2'] == request.form['questionAnswer3']):
            flash('2 or more answer options can not be the same', 'error')
            return redirect(url_for('get_admin_users_new'))
            
        # Inicializamos el objeto que contiene la informacion de la pregunta
        created_question = WebQuestion.create_question(
            backend_service,
            request.form["questionName"], 
            request.form["description"], 
            request.form["questionAnswer"],
            request.form["questionAnswer2"],
            request.form["questionAnswer3"],
            request.form["correctAnswer"],
            request.form["puntuation"],
            request.form["penalty"]
        )

        # si no se ha creado una pregunta, se cargará de nuevo el formulario de crear pregunta. 
        if not created_question:
            return redirect(url_for('get_teacher_questions_new')) 

        #Obtenemos la ruta de redireccion
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            redirect_to = url_for('get_teacher_questions')
        
        # Redireccionamos a la ruta
        return redirect(redirect_to)

    @staticmethod
    def get_teacher_questions_edit(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET request for a question edited by the teacher.
        Args:
            - auth_service (AuthService): The authentication service.
        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))
        id: int = int(request.args.get('id'))
        redirect_to: str = str(request.args.get(
            'redirect_to', default='/teacher/questions'))
        name = session['user']
        return render_template('teacher/questions/edit.html', name=name, roles=session['roles'], question = WebQuestion.get_question(backend_service, id), redirect_to=redirect_to)

    @staticmethod
    def post_teacher_questions_edit(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the POST request for a question edited by the teacher.
        Args:
            - auth_service (AuthService): The authentication service.
        Returns:
            - Union[Response,Text]: The generated response to the request.
        """


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))
        successful: bool = True
 
        successful &= WebQuestion.edit_question(backend_service,
                                                request.form['id'],
                                                request.form['questionName'],
                                                request.form['description'],
                                                request.form['questionAnswer'],
                                                request.form['questionAnswer2'],
                                                request.form['questionAnswer3'],
                                                request.form['correctAnswer'],
                                                request.form['puntuation'],
                                                request.form['penalty']
                                                )
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            redirect_to = url_for('get_teacher_questions')
        return redirect(redirect_to)


    @staticmethod
    def get_teacher_questions_stats(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ TODO STATS DE CADA PREGUNTA
        """

    @staticmethod
    def get_teacher_studentsStats(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ TODO STATS DE LOS ALUMNOS
        """