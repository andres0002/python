# decorators -> Sirve para agragar funcionalidades before y after.

# name decorator -> "name_decorator" -> es una función que agrega funcionalidad
# antes y despues.
def name_decorator(func):
    def func_update():
        print("Before de llamar a la function.") # before
        func() # code
        print("After de llamar a la function.") # after
    return func_update

# Forma no optima -> start.
def greet():
    print("Hello Andres...")

greet_update = name_decorator(greet)

greet_update()
# Forma no optima -> end.

# Forma optima -> start.
# @name_decorator -> Indica que se va utilizar un decorator con el name "name_decorator".
@name_decorator
def greet():
    print("Hello Pepe...")

greet()
# Forma optima -> end.

# Investigation.
# - Decorators of class -> .
# - Desorators mult -> .
# - etc.