from functions.suma import suma # en la misma ruta.

print(f"Total: {suma(1, 2, 3, 4, 5)}.")

import sys

print(sys)
print(sys.builtin_module_names)
sys.path.append("C:\\developer\\fundamentos\\backend\\Python\\functions")
print(sys.path)

import own # para importar modulo completo.
from own import saludar # para importar lo necesario.

print(f"Hola {own.saludar("Andres")}.")
print(f"Hola {saludar("Andres")}.")
