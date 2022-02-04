# walrus = False
# print(walrus)
# #  using walrus
# print(walrus := True)
# print("*" * int(input("Yulduzchaar miqdorini kiriting: ")))
# #  yolochka
# for i in range(rows := int(input("Yulduzchaar miqdorini kiriting: "))):
#     print("*" * (i + 1))
# print(f"Qatorchalar soni: {rows}")
#
#
# def read_line(file):
#     while line := file.readLine():
#         print(line)


# position slash
def mysum(a: int, b: int, /, c: int) -> int:
    return a + b + c


# print(mysum(a=2, b=4, c=10))
print(mysum(2, 4, c=10))


# keyword arguments requirements
def mysum2(*, a: int, b: int, c: int) -> int:
    return a + b + c


# print(mysum(a=2, b=4, c=10))
print(mysum2(a=2, b=4, c=10))


# combination arguments requirements
def mysum2(a: int, /, *, b: int, c: int) -> int:
    return a + b + c


# print(mysum(a=2, b=4, c=10))
print(mysum2(2, b=4, c=10))
