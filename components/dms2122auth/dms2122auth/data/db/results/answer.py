""" Answer class module.
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, String
from sqlalchemy.log import instance_logger  # type: ignore
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer  # type: ignore
from dms2122auth.data.db.results.resultbase import ResultBase


class Answer(ResultBase):
    """ Definition and storage of user ORM records.
    """

    def __init__(self, questionId: str, answer:str, valoration:str):
        """ Constructor method.
        """
        self.questionId: str = questionId
        self.answer: str =  answer
        self.valoration :str =  valoration

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:

        return Table(
            'answer',
            metadata,
            Column('questionId', String(32), primary_key=True),
            Column('answer', String(256), nullable=False),
            Column('valoration', String(64), nullable=False),

        )

