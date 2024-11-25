import asyncio
import gen_it

async def main():
    async for _ in gen_it.start_gen():
        k = _
        print(k.get_c())

asyncio.run(main())
