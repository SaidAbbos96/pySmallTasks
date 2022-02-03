import random
import itertools
# simple generator numbers


def simple_randoms(min: int, max: int, n: int) -> list:
    return [random.randint(min, max) for step in range(n)]


print(simple_randoms(10, 100, 5))

# generation numbers use generator yield
def gen_randoms(min: int, max: int, n:int):
    for step in range(n):
        yield random.randint(min, max)

print(gen_randoms(100,1000, 5))
numbers = gen_randoms(100,1000, 5)
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