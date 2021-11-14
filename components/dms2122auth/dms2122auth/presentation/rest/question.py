""" REST API controllers responsible of handling the user operations.
"""

from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app
from dms2122auth.service import QuestionServices


def list_questions() -> Tuple[List[Dict], Optional[int]]:
    """ Gets the list of question dictionaries.

        Returns:
            - Tuple: Question dictionaries.
            - Optional: boolean 1 or 0 in case the petition was succesfull.
        """
    with current_app.app_context():
        questions: List[Dict] = QuestionServices.list_questions(current_app.db)
    return (questions, HTTPStatus.OK.value)

 