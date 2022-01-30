# my_word = "Bu list comprehension"
# chars_list = [char for char in my_word]
# print(chars_list)
# chars_list = [char for char in my_word if char.isascii() and char != " "]
# print(chars_list)
# chars_list = [char.upper() for char in my_word]
# print(chars_list)
# chars_list = [f"-{char}-" for char in my_word]
# print(chars_list)

# numbers = [num for num in range(0, 100 + 1)]
# print(numbers)
# numbers = [num**2 for num in range(0, 10 + 1)]
# print(numbers)
# numbers = [num for num in range(0, 100 + 1) if num % 2 != 0]
# print(numbers)
# numbers = [num for num in range(0, 100 + 1) if num % 2 == 0]
# print(numbers)

# list_santimetrs = [12, 23, 9, 6, 18, 160, 474]
# list_inches = [round(sm / 2.54, 2) for sm in list_santimetrs]
# print(list_inches)


# list1 = [2, 4, -5, 6, 8, -2]
# list2 = [2, -6, 8, 3, 5, -2]

# qarama_qarshilar = []
# for x in list1:
#     for y in list2:
#         if x+y == 0:
#             qarama_qarshilar.append((x, y))

# print(qarama_qarshilar)  # [(2, -2), (-5, 5), (6, -6), (-2, 2)]

# # endi yuqoridagi uslub bn klass
# qarama_qarshilar2 = [(x, y) for x in list1 for y in list2 if x+y == 0]
# print(qarama_qarshilar2)  # [(2, -2), (-5, 5), (6, -6), (-2, 2)]


first_list = range(11)
second_list = range(11,21)

joined_list = [num for num in first_list if num % 2] + [num for num in second_list if num % 2 != 1]

print(joined_list)