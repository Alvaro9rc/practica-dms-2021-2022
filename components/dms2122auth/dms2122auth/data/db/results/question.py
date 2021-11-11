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

    def __init__(self, questionName: str, description:str, questionAnswer:str, questionAnswer2:str, questionAnswer3:str, puntuation, penalty):
        """ Constructor method.
        """
        self.questionName: str = questionName
        self.description: str =  description
        self.questionAnswer :str =  questionAnswer
        self.questionAnswer2 :str= questionAnswer2
        self.questionAnswer3 :str= questionAnswer3
        self.puntuation :int= puntuation
        self.penalty :int= penalty

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:

        return Table(
            'question',
            metadata,
            Column('questionName', String(32), primary_key=True),
            Column('description', String(256), nullable=False),
            Column('questionAnswer', String(64), nullable=False),
            Column('questionAnswer2', String(64), nullable=False),
            Column('questionAnswer3', String(64), nullable=False),
            Column('puntuation', Integer, nullable=False),
            Column('penalty', Integer, nullable=False)

        )
