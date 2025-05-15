# re -> Module utilizado para trabajar con expresiones regulares.
import re

text_chain = """Hello World
Hello Andres
0123456789
.com
!"#$%&/()=?¡¿'¨~{}[]`^-_,<>|°¬*/-+
"""

# operador ternario -> estructura -> value_si_true if validate else value_si_false

# Busca la primera coincidencia y retorna el value, si no devuelve None.
# print(
#     # si es true.
#     re.search("Hellos", text_chain)
#     # condicción.
#     if re.search("Hello", text_chain) == None
#     # si es false.
#     else re.search("Hello", text_chain)[0]
# )

# Busca todas las coincidencias y las retorna en una list con los values encontrados,
# si no devuelve una lista [].
# print(re.findall(".com", text_chain))

# r -> Nos sirve para indicar que se van a usar expresiones regulares.

# \d -> Busca digitos numéricos del 0 - 9.
# print(re.findall(r"\d", text_chain))

# \D -> Busca all menos digitos numéricos del 0 - 9.
# print(re.findall(r"\D", text_chain))

# \w -> Busca caracteres alfanuméricos [a-z A-Z 0-9 _].
# print(re.findall(r"\w", text_chain))

# \W -> Busca all menos caracteres alfanuméricos [a-z A-Z 0-9 _ space \n].
# print(re.findall(r"\W", text_chain))

# \s -> Busca espacios en blanco -> space, tabs, \n.
# print(re.findall(r"\s", text_chain))

# \S -> Busca all menos espacios en blanco -> space, tabs, \n.
# print(re.findall(r"\S", text_chain))

# . -> Busca all menos saltos en line -> \n.
# print(re.findall(r".", text_chain))

# \n -> Busca saltos en line -> \n.
# print(re.findall(r"\n", text_chain))

# \ -> Cancela los caracteres especiales, cancela la función del "." y busca puntos.
# print(re.findall(r"\.", text_chain))

# Buscando una cadena que coincida con numero, seguido de un punto y
# un espacio [0-9 . space].
# print(re.findall(r"\d\.\s", text_chain))

# ^ -> Busca el comienzo de una linea, y se usa en conjunto con lo que se
# desea encontrar.
# print(re.findall(r"^Hello", text_chain)) # una linea.
# IGNORECASE -> para buscar sin importar si los caracteres están en mayusculas
# o minusculas.
# print(re.findall(r"^Hello", text_chain, flags=re.IGNORECASE))
# print(re.findall(r"^Hello", text_chain, flags=re.M)) # M -> mas de una linea.

# $ -> Busca el final de una linea, y se usa en conjunto con lo que se
# desea encontrar.
# print(re.findall(r"s$", text_chain, flags=re.M))

# {n} -> Busca una cadena con n cantidad de veces el value a la izquierda.
# print(re.findall(r"\d{2}", text_chain)) # dos digitos [0-9].

# {n (min),m (max)} -> Busca una cadena con al menos n y maáximo m.
# print(re.findall(r"\d{1,2}", text_chain)) # dos digitos [0-9].
# print(re.findall(r"(es){1,4}", text_chain)) # conjuntos (es).
# print(re.findall(r"[es]{1,4}", text_chain)) # combinaciones [es].

# | -> Busca un value o el otro.
# print(re.findall(r"\d{3}|\d{1}", text_chain))

# * -> Que puede o no encontrar [0-mas].
# print(re.findall(r"^Hello.*World$|^Hello.*Andres$", text_chain, flags=re.M))

# + -> Que debe encontrar una o mas [1-mas].
# print(re.findall(r"^Hello.+World$|^Hello.+Andres$", text_chain, flags=re.M))

# ? -> Que puede encontrar ninguna o una [0-1] -> optional.
# print(re.findall(r"^Hello.?World$|^Hello.?Andres$", text_chain, flags=re.M))