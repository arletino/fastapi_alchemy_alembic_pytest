from fastapi import Depends, FastAPI
import uvicorn

from app.settings import settings


app = FastAPI()

async def func(param: str, param2: str):
    return {'param': param}

@app.post('/item')
async def read_par(some: str, f: dict = Depends(func)):
    return {
        'some': some,
        'f':f
        }

if __name__ == '__main__':
    uvicorn.run(
        app,
        host=settings.app_host,
        port=settings.app_port,
    )