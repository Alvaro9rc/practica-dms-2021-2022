from typing import Dict
from sqlalchemy import Table, MetaData, Column, String
from sqlalchemy.log import instance_logger  # type: ignore
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer  # type: ignore
from dms2122auth.data.db.results.resultbase import ResultBase


class Answer(ResultBase):
    """ Class Answer
    """

    def __init__(self, id:int, question: int, answer:int, valoration:float, username:str):
        """ Constructor method.

        Initializes a user record.

        Args:
            - questionId (str): A string with the question ID.
            - answer (str): A string with the answer.
            - valoration (str): A string with the valoration.
        """
        self.id: int = id
        self.question: int = question
        self.answer: int =  answer
        self.valoration :float =  valoration
        self.username :str =  username


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
                Column('id', Integer, primary_key=True),
                Column('question', Integer,  nullable=False) ,
                Column('answer', Integer, nullable=False),
                Column('valoration', Integer, nullable=False),
                Column('username', String(64), nullable=False) ,

        )

