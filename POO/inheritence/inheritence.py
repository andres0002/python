class Person:
    def __init__(self, name, age, nacionality):
        self.name = name
        self.age = age
        self.nacionality = nacionality
    
    def show_data(self):
        print(f"Person -> Name: {self.name}, age: {self.age}, nacionality: {self.nacionality}.")

class Employee(Person): # () -> Se usa para poner la clase de la cual se hereda.
    def __init__(self, name, age, nacionality, work, salary):
        # super() -> inheritence simple -> para hacer referencia a la clase father.
        super().__init__(name, age, nacionality)
        self.work = work
        self.salary = salary
    # rescribe el method si se llama igual al del father.
    def show_data(self):
        print(f"Employee -> Name: {self.name}, age: {self.age}, nacionality: {self.nacionality}, work: {self.work}, salary: {self.salary}.")

employee = Employee("Andres", 26, "Colombiana", "Dev", 1500)

employee.show_data()