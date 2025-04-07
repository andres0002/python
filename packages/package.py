import package
import package.saludo
import package.saludo_basic
from package import saludo, saludo_basic
from package.saludo_basic import saludar_basic
from package.saludo import saludar

print(type(package))
print(package)
print(package.__path__)

print(package.saludo_basic.saludar_basic())
print(package.saludo.saludar("Andres"))
print(saludo_basic.saludar_basic())
print(saludo.saludar("Andres"))
print(saludar_basic())
print(saludar("Andres"))

import package.subpackage
import package.subpackage.suma
from package.subpackage import suma
from package.subpackage.suma import suma as funct_suma

print(type(package.subpackage))
print(package.subpackage)
print(package.subpackage.__path__)

print(f"Total: {package.subpackage.suma.suma(1, 2, 3, 4, 5)}.")
print(f"Total: {suma.suma(1, 2, 3, 4, 5)}.")
print(f"Total: {funct_suma(1, 2, 3, 4, 5)}.")