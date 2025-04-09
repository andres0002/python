# MRO (method resolution order) -> método de resolución de orden.

class Person:
    def __init__(self, name, age, nacionality):
        self.name = name
        self.age = age
        self.nacionality = nacionality
    
    def show_data_person(self):
        print(f"Person -> Name: {self.name}, age: {self.age}, nacionality: {self.nacionality}.")
    
    def show_message(self):
        print("Desde person...")

class Artist:
    def __init__(self, skill):
        self.skill = skill
    
    def show_data_artist(self):
        print(f"Artist -> Skill: {self.skill}.")
    
    def show_message(self):
        print("Desde artist...")

class Employee(Person, Artist): # () -> Se usa para poner las clases de la cual se heredan.
    def __init__(self, name, age, nacionality, skill, work, salary):
        # class -> inheritence mult -> para hacer referencia a la clase father.
        Person.__init__(self, name, age, nacionality)
        Artist.__init__(self, skill)
        self.work = work
        self.salary = salary
    
    def show_data_employee(self):
        print(f"Employee -> Name: {self.name}, age: {self.age}, nacionality: {self.nacionality}, skill: {self.skill}, work: {self.work}, salary: {self.salary}.")
    
    def introduce_yourself(self):
        # super() -> para hacer referencia a la clase father.
        super().show_data_person()
        super().show_data_artist()
        # self -> para hacer referencia a la clase current.
        self.show_data_employee()
    
    def show_message(self):
        print("Desde employee...")

employee = Employee("Andres", 26, "Colombiana", "Paint", "Dev", 1500)

employee.introduce_yourself()
employee.show_message()

# orden de jerarquia.
# 0. object -> instancia de class.
# 1. class -> current -> si sobreescribio el método.
# 2. primera class que hereda.
# 3. si de la primera class que hereda no tiene, mira si su ramificación (arbol)
# de herencias si la tenga.
# 4. segunda class que hereda.
# 5. si de la segunda class que hereda no tiene, mira si su ramificación (arbol)
# de herencias si la tenga.
# 6. {n} class que hereda.
# 7. si de la {n} class que hereda no tiene, mira si su ramificación (arbol)
# de herencias si la tenga.

# class.mro() -> para ver el MRO de la class, devuelve la lista en el orden que
# se puede traer ya sea un attribute o method.
print(Employee.mro())

# class.method(instancia -> employee -> Employee) -> para llamar especificamente
# el method o el attribute de una class.
Person.show_message(employee)