from sqlalchemy.orm import mapper, relationship  # type: ignore
from sqlalchemy.sql.sqltypes import Integer, Float

from .question import Question  # type: ignore
from .resultbase import ResultBase
from sqlalchemy import Table, MetaData, Column, String, ForeignKey  # type: ignore
class Answer():
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

    @classmethod
    def map(cls: type, metadata: MetaData) -> None:
        mapper(
            cls,
            Table(
                'answer',
                metadata,
                Column('id', Integer, primary_key=True),
                Column('question', Integer, ForeignKey('question.id'), nullable=False) ,
                Column('answer', Integer, nullable=False),
                Column('valoration', Integer, nullable=False),
                Column('username', String(64), ForeignKey('users.username'), nullable=False) ,

            )
            # ,
            # properties={
            #     'questions': relationship(Question, backref='answer')
            # }
        )