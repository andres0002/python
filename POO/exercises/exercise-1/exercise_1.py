# ------------------------------------Exercise 1-------------------------------------

# Crear una clase estudiante que tenga.

# - Attributes: name, age, grade.
# - Methods: study().

# El method -> study() debe imprimir el siguiente message "El estudiante (name) está
# estudiando".

# Crear una instancia de la class y usar el method study().

# A) Se debe solicitar al user los attributes.
# B) Instanciar la clase y mostrar los datos de la calse creada.
# C) Despues de registrar al estudiante si el user digita "estudiar" (no case sensitive)
# utilizar el method study().

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def show_data_student(self):
        print(f"-----------------------Student {self.name}---------------------------")
        print(f"Name: {self.name}, age: {self.age}, grade: {self.grade}.")
    
    def study(self):
        print(f"El estudiante {self.name} está estudiando.")
    
    def others(self):
        print(f"El estudiante {self.name} está otros.")

# ---------------------Result A-----------------------
name = input("Ingrese el name del student: ")
age = input("Ingrese el age del student: ")
grade = input("Ingrese el grade del student: ")

# ---------------------Result B-----------------------
student = Student(name, age, grade)

student.show_data_student()

# ---------------------Result C-----------------------
print("------------Acciones que puede hacer el student-------------")
print("1. Estudiar -> digite 'estudiar'.")
print("2. Otros -> digite 'cualquier otra cosa'.")
print()
accion_student = input("Ingrese que quiere poner hacer al student: ")

if (accion_student.lower() == "estudiar"):
    student.study()
else:
    student.others()



