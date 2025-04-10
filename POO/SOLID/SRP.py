# SRP -> Single Responsability Principle -> Principio de Responsabilidad Única, Cada componente debe tener una sola
# responsabilidad.

class TankOfFuel:
    def __init__(self):
        self.fuel = 100
    
    def add_fuel(self, amount):
        self.fuel += amount
    
    def get_fuel(self):
        return self.fuel
    
    def use_fuel(self, amount):
        self.fuel -= amount

class Car:
    def __init__(self, tank):
        self.position = 0
        self.tank = tank
    
    def move(self, distance):
        if self.tank.get_fuel() >= distance / 2:
            self.position += distance
            self.tank.use_fuel(distance / 2)
            print("Car moved.")
        else:
            print("No fuel.")
    
    def get_position(self):
        return self.position

tank = TankOfFuel()
car = Car(tank)

car.move(10)
print(f"Car moved {car.get_position()} positions.")
car.move(20)
print(f"Car moved {car.get_position()} positions.")
car.move(40)
print(f"Car moved {car.get_position()} positions.")
car.move(80)
print(f"Car moved {car.get_position()} positions.")
car.move(20)
print(f"Car moved {car.get_position()} positions.")
car.move(50)
print(f"Car moved {car.get_position()} positions.")