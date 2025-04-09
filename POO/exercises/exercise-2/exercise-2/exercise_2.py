# -------------------Inheritence mult and MRO - Exercise 2---------------------------

# Exercise inheritence mult and MRO:

# Imagina que estás modelando animales en un zoo. Crea cuatro classs:

# La class Animal tendrá:
# - Methods: eat().

# La class Mammal tendrá:
# - Inheritence: Animal.
# - Methods: breastfeed().

# La class Bird tendrá:
# - Inheritence: Animal.
# - Methods: fly().

# La class Bat tendrá:
# - Inheritence: Mammal, Bird.
# - Methods: eat(), breastfeed(), fly().

# Finalmenre, juega con el orden de la inheritence de la class Bat y obserba cómo
# cambia el MRO y el comportamiento de los methods al usar super().

class Animal:
    def eat(self):
        print("Animal -> Comer.")

class Mammal(Animal):
    def breastfeed(self):
        print("Mammal -> Amamantar.")

class Bird(Animal):
    def fly(self):
        print("Bird -> Volar.")

class Bat(Mammal, Bird):
    def __init__(self):
        Mammal.__init__(self)
        Bird.__init__(self)
    
    def eat(self):
        print("Bat -> Comer.")
    
    def breastfeed(self):
        print("Bat -> Amamantar.")
    
    def fly(self):
        print("Bat -> Volar.")
    
    def play(self):
        print("--------------------------Playing-------------------------")
        # Referencia a las classs (inheritenceds) supers.
        super().eat()
        super().breastfeed()
        super().fly()
        # Referencia a las class (current).
        self.eat()
        self.breastfeed()
        self.fly()

bat = Bat()

bat.eat()
bat.breastfeed()
bat.fly()

bat.play()

print(Bat.mro())