
def square(*args):
    return [x*x for x in args]


def square_one(num):
    return num*num


def triple(*nums):
    return [num*3 for num in nums]


def is_int(num):
    return isinstance(num, int)

def is_small(age):
    return age < 18

multi = lambda x,y: x*y
lyam_mult_list = lambda *nums: [num*num for num in nums]
if __name__ == "__main__":
    print(square(4, 6, 10))
    print(triple(4, 6, 10))
    print(list(map(square_one, [4, 8, 10])))
    print(list(filter(is_int, [5, "8", 16, 21, "45", "uch"])))
    print(list(filter(is_small, [5, 12, 16, 21, 45, 18, 11])))
    print("shularni hammasini lyamda bn bajaramiz")
    print(square(4, 6, 10))
    print(triple(4, 6, 10))
    print(lyam_mult_list(4,8,5))
    print(multi(4, 5))
    print(list(map(lambda num: num*num, [4, 8, 10])))
    print(list(filter(lambda el: isinstance(el, int), [5, "8", 16, 21, "45", "uch"])))
    print(list(filter(lambda age: age < 18, [5, 12, 16, 21, 45, 18, 11])))