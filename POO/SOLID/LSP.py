# LSP -> Liskov's Substitution Principle -> Principio de Sustitución de Liskov, Los objetos de una clase base pueden
# reemplazarse por objetos de una clase derivada.

# no cumple el principio.
class Bird:
    def fly(self):
        print("I'm flying.")

class Peguin(Bird):
    def fly(self):
        print("I cann't flying.")

def make_fly(bird = Bird):
    return bird.fly()

make_fly(Bird())

# si cumple con el principio.
class Bird:
    pass

class BirdCanFly(Bird):
    def fly(self):
        print("I'm flying.")

class BirdCanNotFly(Bird):
    def fly(self):
        print("I cann't flying.")

make_fly(BirdCanFly())