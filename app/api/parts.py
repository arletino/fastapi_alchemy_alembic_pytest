from fastapi import (
    APIRouter, 
    Depends,
    status
)
from fastapi.responses import JSONResponse

from utils.service_parts import ServicePart

from app.api.models.parts import (
    Part_out,
    Part_in,
    APIPartListResponse,
    APIPartResponse
)


router_parts = APIRouter()

@router_parts.get(
        '/', 
        response_model=APIPartListResponse
        )
async def get_parts(
    parts: ServicePart = Depends(ServicePart.get_parts)
    ) -> JSONResponse:
    response_parts = [part.model_dump_json() for part in parts]
    return JSONResponse(
        content={
            'status': 'ok',
            'data': response_parts
        }
    ) 

@router_parts.get(
        '/{part_art}/',
        response_model=APIPartResponse)
async def get_part_by(
    part_art: str, part: ServicePart = Depends(ServicePart.get_part)
) -> JSONResponse:
    response_part = part.model_dump_json()
    return JSONResponse(
        content={
            'status': 'ok',
            'data': response_part
        }
    )
@router_parts.post(
    '/', 
    response_model=APIPartListResponse,
    status_code=status.HTTP_201_CREATED
    )
async def add_parts(
    parts: list[Part_in] = Depends(ServicePart.add_parts) 
    ) -> JSONResponse:
    data = [part.model_dump() for part in parts]
    return JSONResponse(
        content = {
            'status': 'ok',
            'data': data
        },
        status_code=status.HTTP_201_CREATED
    )

