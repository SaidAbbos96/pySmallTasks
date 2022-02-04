walrus = False
print(walrus)
#  using walrus
print(walrus := True)
print("*" * int(input("Yulduzchaar miqdorini kiriting: ")))
#  yolochka
for i in range(rows := int(input("Yulduzchaar miqdorini kiriting: "))):
    print("*" * (i + 1))
print(f"Qatorchalar soni: {rows}")


def read_line(file):
    while line := file.readLine():
        print(line)

