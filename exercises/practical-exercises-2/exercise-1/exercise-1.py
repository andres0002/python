# ----------------------------------------Exercise 1------------------------------------

# Hoy falto el profesor de clases y los chicos se organizarón para armar la suya (clase)
# propia, uno de los alumnos va ser el profesor y otro va ser su asistente.

# A) Pedir el nombre, apellido y la edad de los compañeros que vinieron hoy a clase y
# ordenar los datos de forma ascendente.

# data.
list_alumnos = []

nums_alumnos = int(input("Ingrese el número de alumnos en clase hoy: "))

for id_alumno in range(nums_alumnos):
    print(f"-------------------------Alumno {id_alumno + 1}----------------------------")
    list_alumnos.append(
        {
            "id": id_alumno,
            "name": input("Ingrese el name del alumno: "),
            "lastname": input("Ingrese el lastname del alumno: "),
            "age": int(input("Ingrese la age del alumno: "))
        }
    )

# Lista ordenada de forma ascedente por el age del alumno.
# list_alumnos = sorted(list_alumnos, key = lambda dict : dict["age"]) # ascendente default -> forma uno
list_alumnos.sort(key = lambda dict : dict["age"]) # ascendente default -> forma dos
print("-----------------------------Result A--------------------------------")
print("La lista ordenada ascendentemente por el age del alumno es igual a:")
for alumno in list_alumnos:
    print(f"--------------------Alumno ID -> {alumno["id"]}---------------------------")
    print(f"Id del alumno: {alumno["id"]}.")
    print(f"Name del alumno: {alumno["name"]}.")
    print(f"Lastname del alumno: {alumno["lastname"]}.")
    print(f"Age del alumno: {alumno["age"]}.")
    

# B) El mayor es el profesor y el menor es el asistente.
#   - ¿Quien es quien?.

# data.
alumno_profesor = list_alumnos[-1]
alumno_asistente = list_alumnos[0]
print("-----------------------------Result B--------------------------------")
print("----------------------------Profesor------------------------------")
print(f"ID del alumno: {alumno_profesor["id"]}.")
print(f"Name del alumno: {alumno_profesor["name"]}.")
print(f"Lastname del alumno: {alumno_profesor["lastname"]}.")
print(f"Age del alumno: {alumno_profesor["age"]}.")
print("---------------------------Asistente------------------------------")
print(f"ID del alumno: {alumno_asistente["id"]}.")
print(f"Name del alumno: {alumno_asistente["name"]}.")
print(f"Lastname del alumno: {alumno_asistente["lastname"]}.")
print(f"Age del alumno: {alumno_asistente["age"]}.")