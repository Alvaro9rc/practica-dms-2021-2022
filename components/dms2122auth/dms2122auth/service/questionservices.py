""" QuestionServices class module.
"""

from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2122auth.data.config import AuthConfiguration
from dms2122auth.data.db import Schema
from dms2122auth.data.db.results import Question
from dms2122auth.data.db.resultsets import Questions


class QuestionServices():
    @staticmethod
    def list_questions(schema: Schema) -> List[Dict]:

        out: List[Dict] = []
        session: Session = schema.new_session()
        questions: List[Question] = Questions.list_all(session)
        for question in questions:
            out.append({
                'id': question.id,
                'questionName': question.questionName,
                'description': question.description,
                'questionAnswer': question.questionAnswer,
                'questionAnswer2': question.questionAnswer2,
                'questionAnswer3': question.questionAnswer3,
                'puntuation': question.puntuation,
                'penalty': question.penalty

            })
        schema.remove_session()
        return out

   