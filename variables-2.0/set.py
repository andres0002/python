# Create conjuntos con set() -> .
set = set(["Andres", "Ramirez"])

# Meter un conjunto dentro de otro conjunto.
set2 = frozenset(["data1", "data2"])
set3 = {set2, "data3"}

print(set)
print(set2)
print(set3)

# Teoria de conjuntos (sets).
set = {1, 3, 5, 7}
set2 = {1, 3, 7}

# Validar si un conjunto es un subconjunto de otro -> Devuelve true si lo es
# y false si no lo es.
print("----------------subset------------------")
print(set2.issubset(set))
print(set.issubset(set2))
print(set2 <= set)
print(set <= set2)

# Validar si un conjunto es un superconjunto de otro -> Devuelve true si lo es
# y false si no lo es.
print("----------------------superset-------------------")
print(set2.issuperset(set))
print(set.issuperset(set2))
print(set2 > set)
print(set > set2)

# Validar (totalmente distinto) si hay algún número en común -> Devuelve true si no
# hay ningún número en común y false si hay algún número en común.
print("----------------------número en común-------------------")
print(set2.isdisjoint(set))
print(set.isdisjoint(set2))
