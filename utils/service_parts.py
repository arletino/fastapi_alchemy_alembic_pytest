import asyncio
import contextlib
import logging

from sqlalchemy import select

from pydantic import ValidationError

from orm.session_manager import (
    get_session,

)
from orm.models.parts_model import Part
import orm
from app.settings import settings
from orm.session_manager import AsyncIterator
from app.api.models.parts import Part_out

logger = logging.getLogger()

async def get_parts() -> list[Part]:
    stmt = select(Part)
    async for session in  get_session():
        parts: list[Part] | None = await session.scalars(stmt)
        print(parts)
    lst_parts: list[Part_out] = []
    for part in parts:
        try:
            temp = Part_out.model_validate(part)
            lst_parts.append(temp)
            print(temp.model_dump_json())
        except ValidationError as e:
            print(e.errors())
            break
    return lst_parts    