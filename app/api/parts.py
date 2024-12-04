
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.parts import Part_out
router_parts = APIRouter()


@router_parts.get('/parts/', )
async def get_parts(parts: list[Part_out] = Depends(get_parts)) -> JSONResponse:
    response_parts = [part.model_dump() for part in parts]
    return JSONResponse(
        content={
            'status': 'ok',
            'data': response_parts
        }
    ) 

