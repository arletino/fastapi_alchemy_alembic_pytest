'''Base Model for DB'''
import uuid

from sqlalchemy import (
    DateTime,
    UUID
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy.sql import (
    func
)

from orm.orm_model import OrmBase

class BaseModel(OrmBase):
    __tablename__ = 'OrmBase'
    
    def __init__(self):
        super().__init__()
        self.__tablename__ = f'{type(self).__name__}s'

    id: Mapped[int] = mapped_column(UUID(as_uuid=True), name=f'OrmBase_id', primary_key=True, default=uuid.uuid4)

    hashtags: Mapped[str | None] = None
    create_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        insert_default=func.now() 
    )    
    update_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )
    comment: Mapped[str | None]  = None

