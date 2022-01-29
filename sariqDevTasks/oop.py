class Person():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def update_age(self):
        self.age += 1
        return self.get_info()

    def get_gender(self):
        return self.gender

    def get_info(self):
        return f"To'liq ism:{self.first_name} {self.last_name}, Yosh: {self.age}, Jinsi: {self.gender}"


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
print(student1.get_info())


def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods("salom"))
