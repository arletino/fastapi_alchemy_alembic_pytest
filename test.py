from orm.models.base_model import BaseModel
from sqlalchemy.orm import Mapped

class NewModel(BaseModel):
    new_field: Mapped[str | None] = None

b = NewModel()
print(b.__tablename__)
