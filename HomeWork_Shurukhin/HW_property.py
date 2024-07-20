class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("Имя должно содержать только буквы!")

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self.__age = new_age
        else:
            print("Возраст должен содержать только цифры!")

    @age.deleter
    def age(self):
        del self.__age


person1 = Person("Irina", 26)
person2 = Person("Igor", 31)
print(person1.__dict__)
print(person2.name)
print(person2.age)
del person1.name
print(person1.__dict__)
