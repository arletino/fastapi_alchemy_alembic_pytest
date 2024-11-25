import contextlib

@contextlib.asynccontextmanager
async def gen():
    print('start gen')
    async with AsyncIterator() as iter:
        yield iter
    print('stop gen')

async def start_gen():
    print('start start_gen')
    async with gen() as g:
        yield g
        print('stop gen1')

async def g():
    print('g')
    yield 
    print('stop g')

class AsyncIterator:
    def __init__(self):
        self.counter = 0
        print('init', self.counter)

    def get_c(self):
        return self.counter
    
    def __aiter__(self):
        print('aiter')
        return self
    
    async def __aenter__(self):
        print('enter in test')
        return self
    
    async def __aexit__(self, exc_type, exc_value, exc_tb):
        print('exit from test')

    async def __anext__(self):
        print('anext', self.counter)
        if self.counter >= 2:
            raise StopAsyncIteration
        self.counter += 1
        return self.counter