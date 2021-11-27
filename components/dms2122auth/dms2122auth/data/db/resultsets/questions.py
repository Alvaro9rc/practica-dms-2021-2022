""" Questions class module.
"""

import hashlib
from typing import List, Dict
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
# from dms2122backend.data.db.orm.results import Question
from dms2122auth.data.db.results import Question
from dms2122auth.data.db.exc import UserExistsError

class Questions():
    """ Class Question. (no utilizada en esta entrega)
    """
    @staticmethod
    def list_all(session: Session) -> List[Dict]:
    # def list_all(session: Session) -> List[Question]:
        """ Gets the list of questions from the database.

        Args:
            - session (Session): The session object.

        Returns:
            - List: A list object with the questions.
        """
        # query = session.query(Question)
        # return query.all()
        out: List[Dict] = []
        out.append(
            {
                'id': 1,
                'questionName': "¿Quién Inventó la luz?",
                'description': "Esto es una pregunta",
                'questionAnswer': "La luz ya existía",
                'questionAnswer2': "Alberto Porres",
                'questionAnswer3': "Guttemberg",
                'puntuation': 20,
                'penalty':10,
                'userCreated': 1


            })
        out.append({
                'id': 2,
                'questionName': "¿Cuántas Patas tiene un caballo?",
                'description': "Pregunta fácil para aprobar",
                'questionAnswer': "Tiene cola",
                'questionAnswer2': "Tiene 4 patas",
                'questionAnswer3': "No existen los caballos",
                'puntuation': 10,
                'penalty': 5,
                'userCreated': 1

            })
        out.append({
                'id': 3,
                'questionName': "Cuál es el radio de la tierra? en km",
                'description': "Pregunta fácil para aprobar",
                'questionAnswer': "6700 km",
                'questionAnswer2': "8000 km",
                'questionAnswer3': "7700 km",
                'puntuation': 10,
                'penalty': 20,
                'userCreated': 1

            })
        return out

   