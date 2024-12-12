from fastapi import Depends, FastAPI
import uvicorn
from typing import Annotated, Any

from app.settings import settings


app = FastAPI()

class Func:
    def __init__(self, a: str, b: str):
        self.a = a
        self.b = b
        
    async def test(self, a: str, b: str):
        return 'work'
    
@app.post('/item')
async def read_par(some: str, f: Annotated[Func, Depends()]):
    data = f.test()
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