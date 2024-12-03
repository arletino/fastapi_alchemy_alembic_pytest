import asyncio
import contextlib

from sqlalchemy import select

from session_manager import get_session
from .models.parts_model import Part


@contextlib.asynccontextmanager
async def connect_db() -> AsyncIterator[None]:
    orm.db_manager.init(settings.database_url)
    yield
    await orm.db_manager.close()
async def get_posts() -> list[Part]:
    stmt = select(Part)
    session = await get_session()
    parts: list[Part] | None = await session.scalars(stmt)
    return parts

async def main():
    parts = await get_posts()
    print(parts)

if __name__ == '__main__':
   asyncio.run(main) 