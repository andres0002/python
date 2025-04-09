class Person:
    # __init__ -> Define un constructor.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # __str__ -> Devuelve un string en representación del object, se pasa data deseada.
    def __str__(self):
        return f"__str__ -> Person(name={self.name}, age={self.age})"
    
    # __repr__ -> Reconstruye el object, requiere una estructura.
    def __repr__(self):
        # se pasa la data en el mismo orden del __init__ (constructor).
        print("__repr__")
        return f"Person('{self.name}',{self.age})"
    
    # para controlar ciertas acciones, en este caso suma.
    def __add__(self, other):
        new_value = self.age + other.age
        return Person(self.name + other.name, new_value)
    
    # para controlar ciertas acciones, en este caso mult.
    def __mul__(self, other):
        new_value = self.age * other.age
        return Person(self.name + other.name, new_value)

person = Person("Andres", 26)
person2 = Person("Pepe", 20)
person3 = Person("Juan", 14)

print(person) # __str__.

print(repr(person)) # __repr__.
print(eval(repr(person))) # para eval hay que representar a los attributes de forma correcta.

print(person + person2 * person3) # __add__ and __mul__.

# Investigation.
# - Sobre carga de operadores.