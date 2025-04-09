class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    # getters
    @property
    def name(self):
        return self.__name
    
    # setters
    @name.setter
    def name(self, name):
        self.__name = name
    
    # deleters
    @name.deleter
    def name(self):
        del self.__name
    
    # getters
    @property
    def age(self):
        return self.__age
    
    # setters
    @age.setter
    def age(self, age):
        self.__age = age
    
    # deleters
    @age.deleter
    def age(self):
        # del -> Sirve para eliminar attributes o properties.
        del self.__age


person = Person("Andres", 26)

# para obtener attributes with getters.
print(f"Name: {person.name}, age: {person.age}.")

# para modificar attributes with setters.
person.name = "Pepe"
person.age = 20

# para eliminar attributes o properties with deleters.
# del person.name
# del person.age

# para obtener attributes with getters.
print(f"Name: {person.name}, age: {person.age}.")