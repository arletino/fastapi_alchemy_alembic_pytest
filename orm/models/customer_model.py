'''Модель описания таблицы дынных клиентов.'''
import uuid
from datetime import datetime
from pathlib import Path

from orm.orm_model import OrmBase

from sqlalchemy.orm import (
    Mapped, 
    mapped_column
)
from sqlalchemy import (
    UUID, 
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func


class Customer(OrmBase):
    '''Information table customers.'''

    __tablename__ = 'customers'

    customer_id: Mapped[int] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
        )
    cust_id: Mapped[int]
    customer_name_ru: Mapped[str]
    customer_name_en: Mapped[str | None] = None
    company_type: Mapped[str | None] = None
    region_ru: Mapped[str | None] = None
    region_en: Mapped[str | None] = None
    hashtags: Mapped[str | None]
    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        insert_default=func.now() 
    )    
    update_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )
    comment: Mapped[str | None]

