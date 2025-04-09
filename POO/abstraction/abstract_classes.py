# abstract class -> es una class que no se puede instanciar, pero se puede
# inheritence de ella, se puede utilizar solo como receta o plantilla,
# es como hacer un contracto que indica que se debe implementar
# de forma obligatoria.

# ABC -> Sirve para establecer classes abstractas.
# abstractmethod -> Sirve para establecer methods abstractos.
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def __init__(self, name, age, sex, activite):
        self.name = name
        self.age = age
        self.sex = sex
        self.activite = activite
    
    @abstractmethod
    def make_activite(self):
        pass
    
    def introduce_yourself(self):
        print(f"Person -> Name: {self.name}, age: {self.age}, sex: {self.sex}, activite: {self.activite}.")

class Student(Person):
    def __init__(self, name, age, sex, activite):
        super().__init__(name, age, sex, activite)
    
    def make_activite(self):
        print(f"Estoy estudiando: {self.activite}.")

class Employee(Person):
    def __init__(self, name, age, sex, activite):
        super().__init__(name, age, sex, activite)
    
    def make_activite(self):
        print(f"Estoy trabajando: {self.activite}.")

# person = Person("Andres", 26, "M", "Dev") -> no se permite instanciar una class abstract.

student = Student("Andres", 26, "M", "Programming")
student.introduce_yourself()
student.make_activite()

employee = Student("Andres", 26, "M", "Dev")
employee.introduce_yourself()
employee.make_activite()