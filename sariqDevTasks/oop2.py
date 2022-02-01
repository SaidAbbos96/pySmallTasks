class Character():
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
class Name():
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


human = Name("BAhoDir", "eshOnoV")
print(human.first_name)
print(human.last_name)
print(human.full_name)
print(human.initials)
