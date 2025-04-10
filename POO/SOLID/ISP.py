# ISP -> Interface Segregation Principle -> Principio de Segregación de Interfaces, No se debe obligar a los consumidores
# a depender de interfaces que no utilizan.

from abc import ABC, abstractmethod

class Work(ABC):
    @abstractmethod
    def work(self):
        pass

class Eat(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleep(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Eat, Work, Sleep):
    def eat(self):
        print("Human is eating.")
    
    def work(self):
        print("Human is working.")
    
    def sleep(self):
        print("Human is sleeping.")

class Robot(Work):
    def work(self):
        print("Robot is working.")

human = Human()
human.eat()
human.work()
human.sleep()

robot = Robot()
robot.work()