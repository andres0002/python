import module_saludar # importa el module completo.
import module_saludar as m_saludar # importa el module completo.

print(type(module_saludar))
print(module_saludar.saludar("Pepe"))
print(type(m_saludar))
print(m_saludar.saludar("Pepe"))

from module_saludar import saludar # importa solo lo necesario.
from module_saludar import saludar as s1, saludar_basic as s2 # importa solo lo necesario.
from module_saludar import * # para importar todo, mala practica.

print(type(saludar))
print(saludar("Pepe"))
print(type(s1))
print(type(s2))
print(s1("Pepe"))
print(s2())

# Para ver propiedades y methods del namespace.
print(dir(m_saludar))

# Para acceder al name del module main este.
print(__name__)

# Para acceder al name del module importado o llamado.
print(m_saludar.__name__)

# Para que se ejecute una ves se ejecute este module.
if __name__ == "__main__":
    print("XD")