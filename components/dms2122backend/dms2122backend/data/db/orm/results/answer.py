from typing import Dict
from sqlalchemy.log import instance_logger  # type: ignore
from sqlalchemy.orm import mapper, relationship  # type: ignore
from sqlalchemy.sql.sqltypes import Integer  # type: ignore
from .resultbase import ResultBase
from sqlalchemy import Table, MetaData, Column, String, ForeignKey  # type: ignore
class Answer(ResultBase):
    """ Class Answer
    """

    def __init__(self, id:str, questionId: str, answer:str, valoration:str):
        """ Constructor method.

        Initializes a user record.

        Args:
            - questionId (str): A string with the question ID.
            - answer (str): A string with the answer.
            - valoration (str): A string with the valoration.
        """
        self.id: str = id
        self.questionId: str = questionId
        self.answer: str =  answer
        self.valoration :str =  valoration

        @classmethod
        def map(cls: type, metadata: MetaData) -> None:
            mapper(
            cls,
            Table(
                'answer',
                metadata,
                Column('id', String(64), primary_key=True),
                Column('questionId', String(32), ForeignKey('question.id'), nullable=False) ,
                Column('answer', String(64), nullable=False),
                Column('valoration', String(64), nullable=False),

            )
        )