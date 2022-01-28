myList = [15, 25, 2, 33, 58, 45, 16, 9, 85, 99]

def maxval(list):
    res = 0
    i = 0
    for el in list:
        i+=1
        if el > res:
            res = el
    print(i)
    return res


def sort(list):
    res = []
    for n in range(len(list)):
        elt = maxval(list)
        res.append(elt)
        list.remove(elt)
    return res

print(sort(myList))