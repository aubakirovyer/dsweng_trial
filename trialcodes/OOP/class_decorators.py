from abc import ABC, abstractmethod
class Person:
    origin_country = "USA"

    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def speak(self, words):
        print(f"{self.name} speaks: {words}")

    @property
    def email(self):
        return f'{self.name}.{self.surname}@email.com'

    @classmethod
    def change_origin_country(cls, new_country):
        cls.origin_country = new_country
        print(cls.origin_country)

    @staticmethod
    def is_adult(age):
        return age > 18

Berik = Person("Berik", "Baltabay", 2323, "M")
Oiken = Person("Oiken", "Amantay", 21, "M")
print(Berik.origin_country)
print(Oiken.origin_country)

Berik.change_origin_country("UK")
print(Oiken.origin_country)

print(Person.is_adult(23))
print(Berik.email)


class Animal(ABC):
    @abstractmethod
    def eat(self):
        raise NotImplementedError
    
class Dog(Animal):
    def eat(self):
        print("Dog is eating!")

doggy = Dog()
doggy.eat()
