
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession 

import orm
from orm.session_manager import AsyncSession

router_parts = APIRouter()


@router_parts.get('/parts/', )
async def get_parts(session: AsyncSession = Depends(orm.get_session())) -> JSONResponse:
    parts_db = await session.scalar(select(orm.Part))

