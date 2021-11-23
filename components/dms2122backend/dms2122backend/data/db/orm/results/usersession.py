from sqlalchemy import Table, MetaData, Column, String, ForeignKey  # type: ignore
from sqlalchemy.orm import mapper  # type: ignore


class UserSession():
    def __init__(self, token: str, username: str):
        self.token: str = token
        self.username: str = username

    @classmethod
    def map(cls: type, metadata: MetaData) -> None:
        mapper(
            cls,
            Table(
                'user_sessions',
                metadata,
                Column('token', String(36), primary_key=True),
                Column('username', String(32),
                       ForeignKey('users.username'), nullable=False)
            )
        )
    