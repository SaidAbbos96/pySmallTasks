from translater import translater


def listUpperCase(words: list) -> list:
    return list(map(lambda word: word.upper(), words))


def listLowerCase(words: list) -> list:
    return list(map(lambda word: word.lower(), words))


def listTitleCase(words: list) -> list:
    return list(map(lambda word: word.title(), words))


def getArea(r: float):
    pi = 3.14159
    """Doiraning yuzini qaytaruvchi funksiya"""
    return pi*(r**2)


def getPerimeter(r: float):
    pi = 3.14159
    """Doiraning perimetrini qaytaruvchi funksiya"""
    return 2*pi*r


def is_admin(login: str, password: str):
    admin = {
        "login": "EngKattaAdmin",
        "password": "Parol123321"
    }
    return admin["login"] == login and admin['password'] == password


if __name__ == "__main__":
    print(translater("Salom"))
    print(translater("Бугун"))
    print(listUpperCase(("salom", "hayr", "yoshlik")))
    print(listLowerCase(("salom", "hayr", "yoshlik")))
    print(listTitleCase(("salom", "hayr", "yoshlik")))
    print(listTitleCase(["Odam", "BOBO", "Hayot", "Sog'lik"]))
    print(is_admin(login="EngKattaAdmin", password="Parol123321"))
