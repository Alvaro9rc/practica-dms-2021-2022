""" Question class module.
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, String
from sqlalchemy.log import instance_logger  # type: ignore
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer  # type: ignore
from resultbase import ResultBase


class Question(ResultBase):
    """ Class Question.
    """

    def __init__(self, id:str,  questionName: str, description:str, questionAnswer:str, questionAnswer2:str, questionAnswer3:str, puntuation:str, penalty:str):
        """ Constructor method.

        Initializes a user record.

        Args:
            - id (str): A string with the question ID.
            - questionName (str): A string with the name.
            - description (str): A string with the description.
            - questionAnswer (str): A string with the first answer.
            - questionAnswer2 (str): A string with the second answer.
            - questionAnswer3 (str): A string with the third answer.
            - puntuation (str): A string with the puntuation.
            - penalty (str): A string with the penalty.
        """
        self.id: str = id
        self.questionName: str = questionName
        self.description: str =  description
        self.questionAnswer :str =  questionAnswer
        self.questionAnswer2 :str= questionAnswer2
        self.questionAnswer3 :str= questionAnswer3
        self.puntuation :str= puntuation
        self.penalty :str= penalty

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
            'question',
            metadata,
            Column('id', String(64),primary_key=True),
            Column('questionName', String(32), nullable= False),
            Column('description', String(256), nullable=False),
            Column('questionAnswer', String(64), nullable=False),
            Column('questionAnswer2', String(64), nullable=False),
            Column('questionAnswer3', String(64), nullable=False),
            Column('puntuation', String(64), nullable=False),
            Column('penalty', String(64), nullable=False)

        )
