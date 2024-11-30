from datetime import datetime

import uuid

from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column

from orm.base_model import OrmBase


class Part(OrmBase):
    '''
    Модель Part - таблица запасные части.
    '''
    __tablename__ = 'parts'

    id: Mapped[int] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    article: Mapped[str | None] = mapped_column(unique=True) 
    article_unit: Mapped[str | None] 
    serial_number_machine: Mapped[str | None]
    alternative_article: Mapped[str | None]
    name_eng: Mapped[str | None] 
    name_ru: Mapped[str | None]
    material: Mapped[str | None]
    weight_kg: Mapped[float | None] 
    size: Mapped[float | None]
    part_type: Mapped[str | None]
    description_custom: Mapped[str | None]
    manufacturer: Mapped[str | None]
    trade_mark: Mapped[str | None]
    qty_in_unit: Mapped[int | None]
    country_eng: Mapped[str | None]
    s_code: Mapped[str | None]
    path_catalog: Mapped[str | None]
    path_documentation: Mapped[str | None]
    path_photo: Mapped[str | None]
    path_avatar: Mapped[str | None]
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