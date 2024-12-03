import asyncio

from sqlalchemy import select

from orm.session_manager import get_session
from orm.models.parts_model import Part

async def get_posts() -> list[Part]:
    stmt = select(Part)
    async for session in get_session():
        parts: list[Part] | None = await session.scalar(stmt)
    return parts

async def main():
    parts = await get_posts()
    print(parts)

if __name__ == '__main__':
   asyncio.run(main()) 