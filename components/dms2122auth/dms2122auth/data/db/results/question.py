""" Question class module.
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, String  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2122auth.data.db.results.resultbase import ResultBase


class Question(ResultBase):
    """ Definition and storage of user ORM records.
    """

    def __init__(self, questionName: str, description:str, questionAnswer:str, IncorrectAnswer:str, IncorrectAnswer2:str, puntuacion, porcentaje):
        """ Constructor method.
        """
        self.questionName: str = questionName
        self.description: str =  description
        self.questionAnswer :str =  questionAnswer
        self.IncorrectAnswer = IncorrectAnswer
        self.IncorrectAnswer2 = IncorrectAnswer2
        self.puntuacion = puntuacion
        self.porcentaje = porcentaje

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:

        return Table(
            'question',
            metadata,
            Column('questionName', String(32), primary_key=True),
            Column('description', String(256), nullable=False),
            Column('questionAnswer', String(64), nullable=False)
            # TODO SEGUIR METIENDO LAS COLUMNAS DE LA TABLA
        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.

        Returns:
            - Dict: A dictionary with the mapping properties.
        """
        return {
            'rights': relationship(Question, backref='question')
        }
