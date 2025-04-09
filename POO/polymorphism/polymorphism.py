# Polimorfismo de inheritence.
class Animal:
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Miauuuuuuuu")

class Dog(Animal):
    def sound(self):
        print("Wauuuuuuuuu")

def make_sound(animal):
    animal.sound()

cat = Cat()
dog = Dog()

# Polimorfismo de object.
cat.sound()
dog.sound()

# Polimosfismo de function.
make_sound(cat)
make_sound(dog)

# Investigation.
# - Duck Typing -> .
# - Enlaces dinámicos -> .
# - Enlaces estáticos -> .
# - Tipo rela -> .
# - Tipo declarado -> .