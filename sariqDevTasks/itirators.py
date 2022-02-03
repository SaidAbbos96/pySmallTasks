import itertools

#  list even numbers
gener = itertools.count(0, 2)
even_nums = [next(gener) for _ in range(10)]
print(even_nums)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#  list odd numbers
gener = itertools.count(1, 2)
odd_nums = [next(gener) for _ in range(10)]
print(odd_nums)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# our enumerate func
list_els = list(zip(itertools.count(0, 3), ["h", "s", "b"]))
print(list_els)  # [(0, 'h'), (3, 's'), (6, 'b')]

rep_char = itertools.repeat("*", 10)
print(rep_char)  # generator
for char in rep_char:  # * * * * * * * * * *
    print(char, end=" ")


list_pows = list(map(pow, range(10), itertools.repeat(2)))
print(list_pows)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# for _ in range(1000000):
#     # TODO
#     print(_)
# for _ in itertools.repeat(None, 1000000):
#     # TODO
#     print(_)


# infinnity generator
# for _ in itertools.cycle(["a", "b"]): a b ab ab ab
#     print(_)
currens = itertools.cycle(["USD", "SUM", "RUB"])
print(list(next(currens) for _ in range(10)))

#  ACCUMALATE
print(list(itertools.accumulate([1, 2, 3, 4, 5, 6])))
print(list(itertools.accumulate([1, 5, 3, 9, 5, 6], max)))
print(list(itertools.accumulate([1, 2, 3, 4, 5, 6], min)))

# chain
print(list(itertools.chain("hello", "world")))
print(list(itertools.chain.from_iterable(["hello", "world"])))

# dropwhile || custom filter
print(list(itertools.dropwhile(
    lambda x: x < 5, sorted([5, 3, 6, 7, 8, 1, 2]))))
# itertools.filterfalse(predicate, iterable)
print(list(itertools.filterfalse(lambda x: x %
      2 == 0, sorted([5, 3, 6, 7, 8, 1, 2]))))
# itertools.groupby(iterable) need a sorted

for key, chars in itertools.groupby(sorted(["s","k","s","a","s","a","s","k","a","k"])):
    print("key: {}, value: {}".format(key, list(chars)))

# itertools.permutations
print(list(itertools.permutations([2,1,5,9])))

# itertools.product()
cardlist = [4, 5, 6,7]
masks = ["B", "S", "X"]
print(list(itertools.product(cardlist, masks)))

lotto_balls = list(range(1, 36+1))
print(lotto_balls)
lotto_balls = list(range(1, 4+1))
print(lotto_balls)
print(len(list(itertools.combinations(lotto_balls, 5))))

