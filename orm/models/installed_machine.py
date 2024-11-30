import uuid
from datetime import datetime

from orm.base_model import OrmBase

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


class InstalledMachine(OrmBase):
    '''Information table installed machine.'''

    __tablename__ = 'installed_machine'

    machine_id: Mapped[int] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    machine_sn: Mapped[str]
    name_short: Mapped[str | None] = None 
    name_full: Mapped[str | None] = None
    customer_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey)
    installation_date: Mapped[DateTime]
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