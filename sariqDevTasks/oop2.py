import math


class Character:
    # Contsanta na urovne classa :) lekin o'zgartirsa bo'ladi Character.__MAX_SPEED = 210
    __MAX_SPEED = 200

    def __init__(self, race, damage=10):
        # Oddiy atrebute obj uchun
        self.damage = damage
        # uslovna privat obj uchun
        self.__race = race
        # atrebut na urovne naslidniki
        self._health = 100

        self._current_speed = 50

    def attack(self, damage: int) -> int:
        self._health -= damage

    @property
    def health(self):
        return self._health

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, speed: int):
        if speed > 100:
            self._current_speed = 100
        elif speed < 0:
            self._current_speed = 0
        else:
            self._current_speed = speed


# kichkina zadachka
class Name:
    def __init__(self, f_name: str, l_name: str):
        self.__first_name = f_name.title()
        self.__last_name = l_name.title()
        # self.first_name = f_name.title()
        # self.last_name = l_name.title()
        # self.fullname = self.first_name + self.last_name
        # self.initials = f"{self.first_name[0]}.{self.last_name[0]}"

    # shu ishlaydi lekin qiyinlashtiramiz
    def __repr__(self):
        return "Ism familiyani tartiblab saqlovchi Oddiy klass"

    @property
    def first_name(self):
        return self.__first_name.title()

    @property
    def last_name(self):
        return self.__last_name.title()

    @property
    def full_name(self):
        return F"{self.__first_name} {self.__last_name}".title()

    @property
    def initials(self):
        return f"{self.__first_name[0]}.{self.__last_name[0]}".upper()


# human = Name("BAhoDir", "eshOnoV")
# print(human.first_name)
# print(human.last_name)
# print(human.full_name)
# print(human.initials)


class Calculator:

    @classmethod
    def add(cls, x, y):
        return x + y

    @classmethod
    def subtract(cls, x, y):
        return x - y

    @classmethod
    def multiply(cls, x, y):
        return x * y

    @classmethod
    def divide(cls, x, y):
        return x / y


# print(Calculator.add(3, 5))
# print(Calculator.subtract(10, 5))
# print(Calculator.multiply(4, 5))
# print(Calculator.divide(81, 9))


class Employee:
    def __init__(self, f_name: str, l_name: str, salary: int):
        self.__first_name = f_name
        self.__last_name = l_name
        self.__salary = int(salary)

    def get_info(self):
        return f"Ishchi obj\nism: {self.first_name }, Familiya: {self.last_name}, Maosh: {self.salary}."

    @property
    def first_name(self):
        return self.__first_name.title()

    @property
    def last_name(self):
        return self.__last_name.title()

    @property
    def salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, scrabe: str):
        datas = scrabe.split("-")
        return Employee(datas[0], datas[1], datas[2])

    def __repr__(self):
        return f"{Employee.__name__} classidan yaratilgan\n{self.get_info()}"


# print(Employee.from_string("Said-bobo-35000000"))

class Pizza:
    __order_number = 0

    def __init__(self, ingredients: list):
        self.__ingredients = ingredients
        Pizza.__order_number += 1
        self.__order_number = Pizza.__order_number

    @property
    def ingredients(self) -> list:
        return self.__ingredients

    @property
    def order_number(self):
        return self.__order_number

    @classmethod
    def order_number(cls):
        return cls.__order_number

    @classmethod
    def orders_count(cls):
        return cls.__order_number

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])


# p1 = Pizza(["bacon", "parmesan", "ham"])
# p2 = Pizza.garden_feast()
# print(p1.ingredients)
# print(p2.ingredients)
# print(p1.order_number())
# print(p2.order_number())
# print(Pizza.orders_count())


class Circle:
    def __init__(self, r=0):
        self.r = r

    def get_area(self):
        return math.pi * self.r ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.r


prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
          "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
          "Pineapple": 3.5}


class Bavarage():
    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.price = self.cost * 2.5

    def get_cost(self):
        return f"${self.cost:.2f}"

    def get_price(self):
        return f"${self.price:.2f}"

    def get_name(self):
        mylist = sorted([i.replace("ies", "y") for i in self.ingredients])
        return f"{' '.join(mylist)} {'Fusion' if len(mylist) > 1 else 'smoothie'}"


obj1 = Bavarage(["Banana"])
print(obj1.ingredients)
print(obj1.get_cost())
print(obj1.get_price())
print(obj1.get_name())

obj2 = Bavarage(["Banana", "Apple"])
print(obj2.ingredients)
print(obj2.get_cost())
print(obj2.get_price())
print(obj2.get_name())

obj3 = Bavarage(["Raspberries", "Strawberries", "Blueberries"])
print(obj3.ingredients)
print(obj3.get_cost())
print(obj3.get_price())
print(obj3.get_name())


# decorator @Final from typing
@Final
class Simple:
    def __init__(self,name)
        self.name = name