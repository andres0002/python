# ---------------------------Inheritence - Exercise 1---------------------------------

# Exercise inheritence and use super():

# Crear un sistema para una escuela. En este sistema, vamos a tener dos classs main:
# Person and Student.

# La class Person tendrá:
# - Attributes: name, age.
# - Methods: show_data_person().

# La class Student tendrá:
# - Inheritence: Person.
# - Attributes: grade.
# - Methods: show_data_student().

# Deberás utilizar super() en el method  de inicialización __init__ para reutilizar
# el código de la class father Person. Luego crea una instancia de la class Student
# e imprime sus attributes y utiliza sus methods para asegurarte de que all funciona
# correctamente.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_data_person(self):
        print(f"Person -> Name: {self.name}, age: {self.age}.")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def show_data_student(self):
        print(f"Student -> Name: {self.name}, age: {self.age}, grade: {self.grade}.")

student = Student("Andres", 26, 11)

student.show_data_person()
student.show_data_student()