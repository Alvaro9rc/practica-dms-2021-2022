""" Question class module.
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, String
from sqlalchemy.log import instance_logger  # type: ignore
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer  # type: ignore
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
        self.IncorrectAnswer :str= IncorrectAnswer
        self.IncorrectAnswer2 :str= IncorrectAnswer2
        self.puntuacion :int= puntuacion
        self.porcentaje :int= porcentaje

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:

        return Table(
            'question',
            metadata,
            Column('questionName', String(32), primary_key=True),
            Column('description', String(256), nullable=False),
            Column('questionAnswer', String(64), nullable=False),
            Column('IncorrectAnswer', String(64), nullable=False),
            Column('IncorrectAnswer2', String(64), nullable=False),
            Column('puntuacion', Integer, nullable=False),
            Column('porcentaje', Integer, nullable=False)

        )
