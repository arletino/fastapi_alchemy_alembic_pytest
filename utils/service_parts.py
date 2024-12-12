import asyncio
import contextlib
import logging

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from pydantic import ValidationError

from orm.session_manager import (
    get_session,

)
from orm.models.parts_model import Part
import orm
from app.settings import settings
from orm.session_manager import AsyncIterator
from app.api.models.parts import (
    Part_in,
    Part_out
)


logger = logging.getLogger(__name__)
logging.basicConfig(datefmt='%Y-%m-%d %H:%M:%S', filename='myapp.log', level=logging.INFO)


class ServicePart:
    async def get_parts() -> list[Part]:
        stmt = select(Part)
        async for session in  get_session():
            parts: list[Part] | None = await session.scalars(stmt)
        parts_out_lst: list[Part_out] = []
        for part in parts:
            try:
                part_out = Part_out.model_validate(part)
                parts_out_lst.append(part_out)
            except ValidationError as e:
                logger.exception(e)
                break
        return parts_out_lst    

    async def get_part(part: Part_in) -> Part_out:
        part_db: Part = Part(**part.model_dump())
        part_db 
        stmt = select(Part).where(part_db)
        async for session in  get_session():
            session.scalars(stmt) 
        
    async def add_parts(parts: list[Part_in]) -> list[Part_in]:
        async for session in get_session():
            part_db = []
            for part in parts:
                part_db.append(Part(**part.model_dump()))
            try:
                session.add_all(part_db)
                await session.flush()
            except IntegrityError as e:
                logger.error(e.args)
                await session.rollback()
                raise 
            await session.commit()                    
        return parts

    async def add_part(part: Part_in) -> None:
        pass    

    async def del_parts(parts: list[Part_in]) -> None:
        pass

    async def del_part() -> None:
        pass