chain1 = "Hola soy WARJ"
chain2 = "Your welcome"

# dir(chain1) func -> Devuelve la lista de atributos y metodos válidos del object pasado.
# print(dir(chain1))

# chain1.upper() -> Convierte los caracteres en mayusculas.
# print(chain1.upper())

# chain1.lower() -> Convierte los caracteres en minusculas.
# print(chain1.lower())

# chain1.capitalize() -> Convierte el primer caracter en mayuscula y los demas los
# convierte en minusculas.
# print(chain1.capitalize())

# chain1.find() -> Busca si esta un value (string) en el string si esta nos devuelve la
# posición donde incia su primer caracter, si no esta nos devuele -1.
# print(chain1.find("soy"))

# chain1.index() -> Busca si esta un value (string) en el string si esta nos devuelve la
# posición donde incia su primer caracter, si no esta nos devuele una exception
# "substring not found".
# print(chain1.index("soy"))

# chain1.isnumeric() -> Devuelve true si es numerico y false si no lo es.
# print(chain1.isnumeric())

# chain1.isalpha() -> Devuelve true si todos los caracteres son alfabéticos
# (a-z and A-Z) y false si no lo es.
# print(chain1.isalpha())

# chain1.count() -> Devuelve cuantas veces aparece un value (string) en un string.
# print(chain1.count("soy"))

# len(chain1) func -> Devuelve cuantos caracteres hay en el string.
# print(len(chain1))

# chain1.startswith("H") -> Devuelve true si el string inicia con el value (string)
# indicado, false si no.
# print(chain1.startswith("H"))

# chain1.endswith("h") -> Devuelve true si el string termina con el value (string)
# indicado, false si no.
# print(chain1.endswith("h"))

# chain1.replace("J", "j") -> Remplaza value (string) por un value (string) indicado y
# devuelve el string modificado, si encuantra el value (substring).
# chain3 = chain1.replace("J", "j")
# print(chain3)

# chain1.split(" ") -> Separa el string deacuerdo al caracter que se indique y devuelve
# una lista. 
array = chain1.split(" ")
print(array)