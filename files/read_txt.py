# open file para poderlo trabajar.
file = open("files\\file.txt", encoding="UTF-8")

# type.
print(type(file))

# leer txt.
# print(file.read())

# leer lineas del txt.
# print(file.readlines())

# leer una sola linea del txt.
print(file.readline())

# cerrar el file (txt) despues de ralizar las acciones requeridas.
file.close()