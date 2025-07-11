class Person:
    origin_country = "USA"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, words):
        print(f"{self.name} speaks: {words}")

    @classmethod
    def change_origin_country(cls, new_country):
        cls.origin_country = new_country
        print(cls.origin_country)

Berik = Person("Berik", 2323, "M")
Oiken = Person("Oiken", 21, "M")
print(Berik.origin_country)
print(Oiken.origin_country)

Berik.change_origin_country("UK")
print(Oiken.origin_country)