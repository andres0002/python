class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age


person = Person("Andres", 26)

print(f"Name: {person.get_name()}, age: {person.get_age()}.")

person.set_name("Pepe")
person.set_age(20)

print(f"Name: {person.get_name()}, age: {person.get_age()}.")