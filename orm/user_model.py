from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .orm_model import OrmBase


class User(OrmBase):
    __tablename__ = 'user_account'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    surname: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f'User(id={self.id!r}, name={self.name!r}, fullname={self.fullname})'