import asyncio
from functools import wraps
from timeit import default_timer as timer


def async_analitic(func):
    @wraps(func)
    async def inner_func(*args, **kwargs):
        start = timer()
        await func(*args, *kwargs)
        print(f"{func.__name__} {timer() - start} soniyada yakunlandi !")

    return inner_func


async def x_o():
    print("X")
    await asyncio.sleep(1)
    print("Y")


@async_analitic
async def main():
    await asyncio.gather(x_o(),x_o(),x_o(),x_o(),x_o())


if __name__ == "__main__":
    pass
    asyncio.run(main())
    # equal to
    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(main())
    #     print("Corotoinlar yakunlandi")
    # finally:
    #     loop.close()
    #     print("Loop is closed !")