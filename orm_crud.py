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
from app.api.models.parts import Part_out, Part_in

logger = logging.getLogger()

@contextlib.asynccontextmanager
async def connect_db() -> AsyncIterator[None]:
    orm.db_manager.init(settings.database_url)
    yield
    await orm.db_manager.close()

async def get_posts() -> list[Part]:
    stmt = select(Part)
    async with connect_db():
        async with get_session() as session:
            parts: list[Part] | None = await session.scalars(stmt)
            print(parts)
    for part in parts:
        try:
            temp = Part_out.model_validate(part)
            print(temp.model_dump_json())
        except ValidationError as e:
            print(e.errors())
            break
    return 

async def get_part(article: str = '151717') -> Part_out:
    stmt = select(Part).where(Part.article == article)
    async with connect_db():
        async for session in get_session():
            parts = await session.scalars(stmt)
            if parts:
                parts_out = list(
                    map(
                        lambda x: Part_out.model_validate(x).model_dump(), 
                        parts
                        )
                    )
                print(parts_out)
                return parts_out
    return None

async def main():
    part = await get_part()


if __name__ == '__main__':
   asyncio.run(main()) 