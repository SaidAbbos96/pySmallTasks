class Person():
    __personCount = 0
    __errors = {
        "not_instance": "Taqqoslash objectlari Person clasiga mansub emas !"
    }

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        Person.__personCount += 1

    def update_age(self):
        self.age += 1
        return self.get_info()

    def get_gender(self):
        return self.gender

    def get_info(self):
        return f"To'liq ism:{self.first_name} {self.last_name}, Yosh: {self.age}, Jinsi: {self.gender}"

    def __repr__(self):
        return f"{self.__class__.__name__} classi inson objectlarini yaratishda shablon vazifasida ishlatiladi !"

    def __lt__(self, y):
        if Person.is_Person(y):
            return self.age < y.age
        return Person.__errors["not_instance"]

    def __gt__(self, y):
        if Person.is_Person(y):
            return self.age > y.age
        return Person.__errors["not_instance"]

    def __le__(self, y):
        if Person.is_Person(y):
            return self.age <= y.age
        return Person.__errors["not_instance"]

    def __ge__(self, y):
        if Person.is_Person(y):
            return self.age >= y.age
        return Person.__errors["not_instance"]

    def __eq__(self, y):
        if Person.is_Person(y):
            return self.age == y.age
        return Person.__errors["not_instance"]

    def __ne__(self, y):
        if Person.is_Person(y):
            return self.age != y.age
        return Person.__errors["not_instance"]

    def __len__(self):
        return len(self.first_name + self.last_name)

    # o'rgandim ammo bu classga ushbu methodlarni bog'lash manisiz.
    def __getitem__(self, index):
        pass

    def __setitem__(self, index):
        pass

    def __call__(self):
        pass

    # arifmetika
    def __add__(self, *arguments):
        pass

    def __sub__(self, arg):
        pass

    def __mul__(self, level):
        pass

    def __pow__(self, xlevel):
        pass

    def __div__(self, diver):
        pass

    @classmethod
    def get_pers_count(cls):
        return cls.__personCount

    @classmethod
    def is_Person(cls, obj):
        return isinstance(obj, Person)

    # umuman olganda bunaqa dundor methodlar juda kop ekan alohida yozib chiqishga vaqt sarflashni istamadim


class Student(Person):
    def __init__(self, first_name, last_name, age, gender, otm, level, id, manzil):
        super().__init__(first_name, last_name, age, gender)
        self.otm = otm
        self.level = level
        self.id = id
        self.manzil = manzil

    def upgrate_level(self):
        self.level += 1
        return self.get_info()

    def set_addres(self, adress):
        self.manzil = adress
        return self.get_info()

    def get_info(self):
        return f"Talaba malumotnomasi:\nTo'liq ism:{self.first_name} {self.last_name}, Yosh: {self.age}, Jinsi: {self.gender}\nOTM: {self.otm}, Bosqich: {self.level}, Student_id: {self.id}\n{self.manzil.get_full_adress()}"


class Adress():
    def __init__(self, countre, provence, street, home_num):
        self.countre = countre
        self.provence = provence
        self.street = street
        self.home_num = home_num

    def get_full_adress(self):
        return f"Full adress: {self.countre}, {self.provence}, {self.street}, {self.home_num}."


student1 = Student("Bahodir", "Eshonov", 25, "Erkak", "Samtatu", 1,
                   "T2565", Adress("Uzbekistan", "Samarkand", "Katta kocha", "N35a"))


pers = Person("Bobojan", "Hikmatov", 45, "Male")
# print(Person.get_pers_count())
# print(Person.is_Person(pers))
print(len(student1))


def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
