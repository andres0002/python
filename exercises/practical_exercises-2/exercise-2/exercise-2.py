# ------------------------------------Exercise 2----------------------------------

# Crear una function que nos devuelva los números primos entre 0 y el num dado.

# forma uno.
# function que validad si el num es primo o no.
def is_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# function que retorna la lista de numero primos entre 0 y el num dado.
def primos_hasta(num):
    list_primos = []
    for i in range(2, num + 1):
        if is_primo(i):
            list_primos.append(i)
    return list_primos

# muestra en console los nums primos.
print(primos_hasta(23))

# forma dos.
primos_hasta = lambda num : list(
    filter(
        lambda x : all(
            x % i != 0 for i in range(2, int(x ** 0.5) + 1) # range(2, x)
        ), range(2, num + 1)
    )
)

# muestra en console los nums primos.
print(primos_hasta(23))