from typing import Dict
from sqlalchemy import Table, MetaData, Column, String
from sqlalchemy.log import instance_logger  # type: ignore
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer  # type: ignore
from dms2122auth.data.db.results.resultbase import ResultBase


class Answer(ResultBase):
    """ Class Answer
    """

    def __init__(self, questionId: str, answer:str, valoration:str):
        """ Constructor method.

        Initializes a user record.

        Args:
            - questionId (str): A string with the question ID.
            - answer (str): A string with the answer.
            - valoration (str): A string with the valoration.
        """
        self.questionId: str = questionId
        self.answer: str =  answer
        self.valoration :str =  valoration

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ Gets the table definition.

        Args:
            - metadata (MetaData): The database schema metadata
                        (used to gather the entities' definitions and mapping)

        Returns:
            - Table: A `Table` object with the table definition.
        """
        return Table(
            'answer',
            metadata,
            Column('questionId', String(32), primary_key=True),
            Column('answer', String(256), nullable=False),
            Column('valoration', String(64), nullable=False),

        )

