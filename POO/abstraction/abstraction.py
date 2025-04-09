# abstraction -> ocultar la complejidad interna de un sistema.
class Car:
    def __init__(self):
        self._state = "off"
    
    def on(self):
        self._state = "on"
        print("Car is on.")
    
    def off(self):
        self._state = "off"
        print("Car is off.")
    
    def driver(self):
        if self._state == "off":
            self.on()
        print("Car in moving.")

car = Car()

# user -> use -> abstraction -> object.
car.on()
car.off()
car.driver()
car.off()