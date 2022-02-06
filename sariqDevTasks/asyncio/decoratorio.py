from timeit import default_timer as timer
from functools import wraps

def async_analitic(func):
    @wraps(func)
    async def inner_func(*args, **kwargs):
        start = timer()
        await func(*args, *kwargs)
        print(f"{func.__name__} {timer() - start} soniyada yakunlandi !")

    return inner_func
