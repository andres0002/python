# list([]) -> Para crear una lista, un buen uso es para lista vacias.
# list = list(["Hola:", "Andres,", "Age:"])
list = list([4, 5, 2, True, False])
print(list)

# " ".join(list) -> Para unir elementos de una lista en un string.
# chain = " ".join(list)
# print(chain + " " + str(26) + ".")

# len(list) -> Devuelve el numero de elementos de la lista.
# print(len(list))

# list.append(26) -> Para agragar un elemento a la lista.
# list.append(26)
# print(list)

# list.insert(26) -> Para agragar un elemento a la lista en un index especifico,
# si el index no es correcto lo agraga al ultimo.
# list.insert(3, 26)
# print(list)

# list.extend([26, "XD"]) -> Para agregar mas de un elemento a la lista.
# list.extend([26, "XD"])
# print(list)

# list.pop(2) -> Para eliminar un elemento de la lista por el index.
# list.pop(-1) -> Para eliminar el ultimo elemento dela lista.
# list.pop(2)
# print(list)

# list.remove("Age:") -> Para eliminar un elemento de la lista por el value, si no
# esta el value devuelve la exception "not in list".
# list.remove("Age:")
# print(list)

# list.clear() -> Para limpiar la lista o eliminar todos los elementos de la lista.
# list.clear()
# print(list)

# list.sort() -> Sirve para ordenar los elementos de la lista, procurar que los
# elementos de la lista sean del mismo type, para ordenar de type str todos los
# elementos de la lista deben ser de type str o da una exceptipon, para ordenar
# numeros se pueden conbinar con valores bool pero no con str por que da una
# exception.
# list.sort(reverse=True) -> Para ordenar de forma descendente.
# list.sort(reverse=False) default -> Para ordenar de forma ascendente.
# list.sort()
# print(list)

# list.reverse() -> Para invertir el orden de la lista, para dar un giro
# de 180° a la lista.
# list.reverse()
# print(list)

# list.index(5) -> Para validar si un elemento esta en la lista, si esta devuelve el
# index del elemento encontrado, si no devuelve una exception "not in list".
print(list.index(5))