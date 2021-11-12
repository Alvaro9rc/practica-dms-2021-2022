# """ Questions class module.
# """

# import hashlib
# from typing import List
# from sqlalchemy.exc import IntegrityError  # type: ignore
# from sqlalchemy.orm.session import Session  # type: ignore
# from sqlalchemy.orm.exc import NoResultFound  # type: ignore
# from dms2122auth.data.db.results import Question
# from dms2122auth.data.db.exc import UserExistsError


# class Questions():

#     @staticmethod
#     def list_all(session: Session) -> List[Question]:
#         query = session.query(Question)
#         return query.all()

   