mylist = [4,10,9,11,5,25,87,2,14,45,13,48]

def bubleSort(arr:list) -> list:
    count = 0
    for i in range(len(arr)):
        for ind in range(len(arr) - i - 1):
            count += 1
            if arr[ind] > arr[ind + 1]:
                arr[ind], arr[ind + 1] = arr[ind + 1], arr[ind]
            print(arr)
    print("Count", count)


bubleSort(mylist)
