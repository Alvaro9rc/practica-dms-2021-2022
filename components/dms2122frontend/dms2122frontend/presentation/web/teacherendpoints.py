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

        '''Endpoint para el creado de preguntas '''

        #Controlamos que el usuario se haya logeado
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        # Inicializamos el objeto que contiene la informacion de la pregunta
        created_question = WebQuestion.create_question(
            auth_service,
            request.form["questionName"], 
            request.form["description"], 
            request.form["questionAnswer"],
            request.form["IncorrectAnswer"],
            request.form["IncorrectAnswer2"],
            request.form["puntuacion"],
            request.form["porcentaje"]
        )

        # si no se ha creado una pregunta, se cargará de nuevo el formulario de crear pregunta. 
        # ahora mismo será todo el tiempo porque no se guarda una pregunta
        if not created_question:
            return redirect(url_for('get_teacher_questions_new')) 

        #Obtenemos la ruta de redireccion
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            redirect_to = url_for('get_teacher_questions')
        
        # Redireccionamos a la ruta
        return redirect(redirect_to)

# editar preguntas
    @staticmethod
    def get_teacher_questions_edit(auth_service: AuthService) -> Union[Response, Text]:

        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))
            # TODO PENDIENTE POR PASAR A ESTA FUNCION EL OBJETO QUESTION PARA QUE SE PINTE EN EL EDIT
        # id: str = str(request.args.get('id'))
        # questionName: str = str(request.args.get('questionName'))
        # description: str = str(request.args.get('description'))
        # questionAnswer: str = str(request.args.get('questionAnswer'))
        # IncorrectAnswer: str = str(request.args.get('IncorrectAnswer'))
        # IncorrectAnswer2: str = str(request.args.get('IncorrectAnswer2'))
        # puntuacion: str = str(request.args.get('puntuacion'))
        # porcentaje: str = str(request.args.get('porcentaje'))
        
        # le llega un objeto a pelo, esto habrá que cambiar
        id: str =1
        questionName: str = "Texto de la pregunta"
        description: str = "Descripción"
        questionAnswer: str ="Texto de la respuesta"
        IncorrectAnswer: str = "Respuesta Incorrecta 1"
        IncorrectAnswer2: str = "Respoesta Incorrecta 2"
        puntuacion: str  = "1"
        porcentaje: str = "20%"
        redirect_to: str = str(request.args.get(
            'redirect_to', default='/teacher/questions'))
        return render_template('teacher/questions/edit.html',id=id, questionName=questionName, description=description, questionAnswer=questionAnswer, IncorrectAnswer=IncorrectAnswer, IncorrectAnswer2=IncorrectAnswer2, puntuacion=puntuacion,porcentaje=porcentaje,
                               redirect_to=redirect_to
                               )

    @staticmethod
    def post_teacher_questions_edit(auth_service: AuthService) -> Union[Response, Text]:

        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))
        successful: bool = True
        #  en lugar de pasar la lista de preguntas para sustituir, pasaremos la pregunta junto con su id. Porque si no, con el teimpo y al añadir x preguntas, no será eficiente
        successful &= WebQuestion.update_teacher_question(auth_service,
                                                request.form['id'],
                                                request.form['questionName'],
                                                request.form['description'],
                                                request.form['questionAnswer'],
                                                request.form['IncorrectAnswer'],
                                                request.form['IncorrectAnswer2'],
                                                request.form['puntuacion'],
                                                request.form['porcentaje']
                                                )
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            redirect_to = url_for('get_teacher_questions')
        return redirect(redirect_to)
