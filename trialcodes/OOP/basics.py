class Person:
    origin_country = "USA"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, words):
        print(f"{self.name} speaks: {words}")

class Employee(Person):
    def __init__(self, name, age, gender, salary, job_title):
        super().__init__(name, age, gender)
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        print(f"Employee {self.name} works as a {self.job_title}")

    
Berik = Employee("Berik", 2323, 'M', 200000, "Logistics Manager")
Berik.speak("I love Dota2")
Berik.display_info()


class DataHide:
    def __init__(self, id, name):
        self.__id = id
        self._name = name

Berik = DataHide(123, "Berik")
print(Berik._name)
print(Berik._DataHide__id)


# multiple inheritances
class Base:
    def call(self):
        print("Base Class")

class Left(Base):
    def call(self):
        print("Left Class")

class Right(Base):
    def call(self):
        print("Right Class")

class Child(Left, Right):
    pass

child = Child()
child.call()