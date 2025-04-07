nums = [1, 2, 3, 4, 5]

# max() -> Encontrando el número mayor de una list o iterable.
num_max = max(nums)
print(f"Num max: {num_max}.")

# min() -> Encontrando el número menor de una list o iterable.
num_min = min(nums)
print(f"Num min: {num_min}.")

# round() -> Redondeando a num de decimales deseados.
num = 222.1234567890
print(f"Num redondeado: {round(num, 6)}.")

# bool() -> return False -> values -> 0, vacio, False, None.
# bool() -> return True -> values -> distinct a 0, True, string.
print(f"bool(): {bool([False, True])}.")

# all() -> Retorna True -> values -> all son verdaderos.
print(f"all(): {all([False, True])}.")

# sum() -> Suma todos los valores de un iterable.
print(f"Sum de nums: {sum(nums)}.")