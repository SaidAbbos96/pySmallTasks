from transliterate import to_latin, to_cyrillic


def translater(string: str) -> str:
    string = string.strip()
    if string.isascii():
        return to_cyrillic(string)
    return to_latin(string)
    # elif not string.isascii():
    #     return to_latin(string)


def go_transletter():
    print("Lotin kerel yoki kerel lotin tartibli tarjimonga hush kelibsiz, matnni kiriiting :")
    while True:
        text = input("Matn: ").strip()
        if len(text) > 0:
            print(translater(text))
        else:
            print("Tarjima qilish uchun matnni kiriting !!!")


if __name__ == "__main__":
    go_transletter()