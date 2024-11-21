from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from orm.base_model import OrmBase


class Part(OrmBase):
    '''
    Модель Part - таблица запасные части.
    '''
    __tablename__ = 'parts'

    id: Mapped[int] = mapped_column(primary_key=True)
    article: Mapped[str | None] 
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
    createAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
        )
    changeAt: Mapped[datetime] = datetime.now()
    comment: Mapped[str | None]