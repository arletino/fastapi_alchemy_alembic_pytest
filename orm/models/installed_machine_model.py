'''Модель для описания таблицы перечня установленных станков.'''
import uuid
from datetime import datetime
from pathlib import Path

from orm.orm_model import OrmBase
from orm.models.customer_model import Customer
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship
)
from sqlalchemy import (
    UUID, 
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func


class InstalledMachine(OrmBase):
    '''Information table installed machine.'''

    __tablename__ = 'installed_machines'

    machine_id: Mapped[int] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
        )
    machine_sn: Mapped[str]
    name_short: Mapped[str | None] = None 
    name_full: Mapped[str | None] = None
    customer_id: Mapped[UUID] = mapped_column(ForeignKey('customer.customer_id'))
    customer: Mapped['Customer'] = relationship('Customer', back_populates='machine')
    date_install: Mapped[DateTime] = None
    city_ru_install: Mapped[str] = None 
    city_eng_install: Mapped[str] = None 
    address_install: Mapped[str] = None 
    docs_path: Mapped[Path] = None
    machine_status: Mapped[str | None] = None
    machine_type: Mapped[str | None] = None
    hashtags: Mapped[str | None] = None
    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        insert_default=func.now() 
    )    
    update_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )
    comment: Mapped[str | None] = None