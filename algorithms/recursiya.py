def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

# print(factorial(5))


def recursiveSum(array):
    if len(array):
        return array[0] + recursiveSum(array[1:])
    return 0


print(recursiveSum([5,3,8]))