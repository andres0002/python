class Person:
    def __init__(self, name, age, nacionality):
        self.name = name
        self.age = age
        self.nacionality = nacionality
    
    def show_data_person(self):
        print(f"Person -> Name: {self.name}, age: {self.age}, nacionality: {self.nacionality}.")

class Artist:
    def __init__(self, skill):
        self.skill = skill
    
    def show_data_artist(self):
        print(f"Artist -> Skill: {self.skill}.")

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

employee = Employee("Andres", 26, "Colombiana", "Paint", "Dev", 1500)

employee.introduce_yourself()

# Para saber si una class es subclass de otra class.
print(f"Employee es subclass de Person: {issubclass(Employee, Person)}")
print(f"Employee es subclass de Artist: {issubclass(Employee, Artist)}")
print(f"Person es subclass de Employee: {issubclass(Person, Employee)}")
print(f"Artist es subclass de Employee: {issubclass(Artist, Employee)}")

# Para saber si un object es una instancia de una class.
print(f"Object employee is instancia de Person: {isinstance(employee, Person)}")
print(f"Object employee is instancia de Artist: {isinstance(employee, Artist)}")
print(f"Object employee is instancia de Employee: {isinstance(employee, Employee)}")