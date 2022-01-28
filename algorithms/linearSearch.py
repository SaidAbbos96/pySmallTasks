"""
Masala:
Bizga quyidagi massiv berilgan:

myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]

Massiv ichidan bizga kerakli qiymatning indeksini (tartib raqamini) linear search yordamida qaytaruvchi funksiya yozing. Agar qidiralayotgan qiymat massiv ichida mavjud bo’lmasa -1 yoki None qiymatini qaytaring.
"""

myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
def linearSearch(list, el):
    if el in list:
        return list.index(el)
    else:
        return None

print(linearSearch(myList1, 15))
print(linearSearch(myList1, 45))