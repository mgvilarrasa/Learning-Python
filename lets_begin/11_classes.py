class Person:
    def __init__(self, name, surname) -> None:
        self.__name = name #__variable -> private attribute
        self.__surname = surname
        self.full_name = f"{name} {surname}"

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def walk(self):
        print("Walking...")

my_person = Person("TestName", "TestSurname")
print(my_person.full_name)
print(my_person.get_name())
print(my_person.get_surname())
my_person.walk()