# Lista (list) -> Se puede modificar.
list = ["WARJ", 26]
list[1] = "XD"

# Tupla (tuple) -> No se puede modificar.
tupla = ("W.A.R.J.", 26)
# tupla[1] = "XD"

# Conjunto (set) -> Para omitir valores repetidos.
# print(conjuntSet[0]) -> No se puede acceder por indice.
conjuntSet = {"W.A.R.J.", 26}

# Dicionario (dict) o json -> key: value.
dicionario = {
    "name": "Andres",
    "age": 26
}

print(type(list))
print(list[0])
print(type(tupla))
print(tupla[0])
print(type(conjuntSet))
print(conjuntSet)
print(type(dicionario))
print(dicionario["name"])