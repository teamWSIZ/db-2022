import asyncio


async def foo():
    print('hello')


async def run_it():
    await foo()
    await foo()
    await foo()

if __name__ == '__main__':
    asyncio.run(run_it())   # "engine" asynchroniczny uruchamiany (even loop)
