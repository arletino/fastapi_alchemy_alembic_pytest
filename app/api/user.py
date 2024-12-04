import uuid
from typing import Literal
from pydantic import (
    BaseModel, 
    ConfigDict, 
    Field
    )

from typing import Literal

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.models.parts import Part_out
import orm
from utils.service_parts import get_parts


class UserCreateRequest(BaseModel):
    
    name: str = Field(max_length=30)
    fullname: str


class UserResponse(BaseModel):
    id: int
    name: str
    fullname: str 

    model_config = ConfigDict(from_attributes=True)

# Используем более гибкую структуру ответов.

class APIUserResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: UserResponse

class APIUserListResponse(BaseModel): 
    status: Literal['ok'] = 'ok'
    data: list[UserResponse]

class APIPartsResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: list[Part_out]

router = APIRouter()

@router.get('/{user_id}/', response_model=APIUserResponse)
async def get_user(
    user_id: int, session: AsyncSession = Depends(orm.get_session)
) -> JSONResponse:
    user = await session.get(orm.User, user_id)
    if not user:
        return JSONResponse(
            content = {'status': 'error', 'messages': 'User not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    response_model = UserResponse.model_validate(user)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': response_model.model_dump(),
        }
    )
@router.get('/test', response_model=APIPartsResponse)
async def get_parts(all: Part_out = Depends(get_parts)) -> JSONResponse:
    parts: list[JSONResponse]= [part.model_dump_json() for part in all]
    return JSONResponse(
        content=parts
        )


@router.get('/', response_model=APIUserListResponse)
async def get_users(session: AsyncSession = Depends(orm.get_session)) -> JSONResponse:
    users_results = await session.scalars(select(orm.User))
    print(users_results)
    response_data = [
        UserResponse.model_validate(u).model_dump() for u in users_results
    ]
    return JSONResponse(
        content={
            'status': 'ok',
            'data': response_data, 
            }
    )
@router.post('/', response_model=APIUserListResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreateRequest, session: AsyncSession = Depends(orm.get_session)
) -> JSONResponse:
    user_candidate = orm.User(**user_data.model_dump())
    session.add(user_candidate)
    # I skip error handling
    await session.commit()
    await session.refresh(user_candidate)
    response_model = UserResponse.model_validate(user_candidate)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': response_model.model_dump(),
        },
        status_code=status.HTTP_201_CREATED
    )