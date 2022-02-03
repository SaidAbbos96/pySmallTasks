import random
import itertools
# simple generator numbers


def simple_randoms(min: int, max: int, n: int) -> list:
    return [random.randint(min, max) for step in range(n)]


print(simple_randoms(10, 100, 5))

# generation numbers use generator yield


def gen_randoms(min: int, max: int, n: int):
    for step in range(n):
        yield random.randint(min, max)


print(gen_randoms(100, 1000, 5))
numbers = gen_randoms(100, 1000, 5)
print(numbers)
for num in numbers:
    print(num)
print(numbers)
# generation not work again
for num in numbers:
    print(num)

# universal generation numbers use generator yield


def gen_randoms(min: int, max: int):
    while True:
        yield random.randint(min, max)


for num in itertools.islice(gen_randoms(2000, 3000), 5):
    print(num)


# read big files step by step use generation in python
def lazy_reading(file):
    while True:
        line = file.readline()
        if not line:
            break
        yield line


file = open(r"sariqDevTasks\test.txt")
for line in lazy_reading(file):
    print(line.rstrip())


# list comprehentiopn using generation
list_nums = [6, 5, 8, 19, 25, 36]
# simple method
squares = [num**2 for num in list_nums]
print(squares)
squares_gen = (num**2 for num in list_nums)
print(squares_gen)
for square in squares_gen:
    print(square)
