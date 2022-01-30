from functools import wraps
from timeit import default_timer as timer
import time


def logging_deco_play(func):
    print(f"{func} Funcsiya boshlandi !!")
    func()
    print(f"{func} Funcsiya yakunlandi !!")


@logging_deco_play
def hello_world_play(greeting_text="Hello World !!!"):
    print(greeting_text)


def logging_deco(func):
    def manager():
        print(f"{func} Funcsiya boshlandi !!")
        func()
        print(f"{func} Funcsiya yakunlandi !!")
    return manager


@logging_deco
def hello_world(greeting_text="Hello World !!!"):
    print(greeting_text)


hello_world()


def measures_time(func):
    def inner_func(*args, **kwargs):
        start = timer()
        func(*args, *kwargs)
        print(f"{func.__name__} {timer() - start} soniyada yakunlandi !")
    return inner_func


@measures_time
def get_list(start, end):
    res = list(range(start, end+1))
    print(res)
    return res


get_list(1, 1000000)


def log_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f"{func.__name__} ishga tushdi !")
        func(*args, **kwargs)
        print(f"{func.__name__} yakunlandi !")
    return wrap


@log_decorator
def greet(text):
    print(text)


greet("salom bro !")
help(greet)
