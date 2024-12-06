
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from utils.service_parts import ServicePart

from app.api.models.parts import (
    Part_out,
    APIPartListResponse
)


router_parts = APIRouter()



@router_parts.get('/', response_model=APIPartListResponse)
async def get_parts(parts: list[Part_out] = Depends(ServicePart.get_parts)) -> JSONResponse:
    response_parts = [part.model_dump_json() for part in parts]
    return JSONResponse(
        content={
            'status': 'ok',
            'data': response_parts
        }
    ) 

