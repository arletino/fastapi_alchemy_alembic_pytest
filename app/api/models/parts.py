from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class Part_in(BaseModel):
    
    article: str | None = None
    article_unit: str | None = None
    serial_number_machine: str | None = None
    alternative_article: str  | None = None
    name_eng: str | None  = None 
    name_ru: str | None = None
    material: str | None = None
    weight_kg: float | None = None
    size: float | None = None
    part_type: str | None = None
    description_custom: str | None = None
    manufacturer: str | None = None
    trade_mark: str | None = None
    qty_in_unit: int | None = None
    country_eng: str | None = None
    s_code: str | None = None
    path_catalog: str | None = None
    path_documentation: str | None = None
    path_photo: str | None = None
    path_avatar: str | None = None
    hashtags: str | None = None
    comment: str | None = None

    class Config:
        coerce_numbers_to_str=True

class Part_out(Part_in): 
    
    id: int
    createAt: datetime 
    changeAt: datetime