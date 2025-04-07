# def name_description() -> Para definir funciones simples.
def saludar():
    print("Hello World...")
# execute -> function.
saludar()

# def name_description(*params) -> Para definir funciones con parametros.
def saludar(name):
    print(f"Hello {name}...")
# execute -> function.
saludar("Andres")

# def name_description(*params) -> Para definir funciones que retornan un value o
# values (iterables).
def saludar(name):
    # return name, 0 # values default (tuple)
    return name # value
# execute -> function.
print(f"Hello {saludar("Andres")}...")

# sum() -> Forma no optima de sumar values.
def suma(iterable):
    total = 0
    for num in iterable:
        total += num
    return total
# execute function.
print(f"Total: {suma([1, 2, 3, 4, 5])}.")

# sum() -> Forma optima de sumar values.
def suma(*nums):
    print(type(nums)) # (tuple)
    return sum(nums)
# execute function.
print(f"Total: {suma(1, 2, 3, 4, 5)}.")