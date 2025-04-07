animals = ["gato", "perro", "loro", "cocodrilo"]
nums = [1, 2, 3, 4] # list
nums = (1, 2, 3, 4) # tuple
nums = {1, 2, 3, 4} # set

# Para iterar una lista.
# for animal in animals:
#     print(f"Animal: {animal}.")
    
# Para iterar mas de una lista al mismo tiempo, tener en cuenta ambas listas deben
# tener el mismo número de elements.
# for num, animal in zip(nums, animals):
#     print(f"Num: {num}, Animal: {animal}.")
    
# Para interar por range, no sirve para sets (conjuntos).
# for num in range(5 start, 10 end):
# for num in range(10 end):
# for num in range(5, 10):
#     print(f"Num del range is: {num + 1}.")
    
# Para iterar una lista y para obtener el index.
# for key, value in enumerate(nums):
#     print(f"Index: {key}, value: {value}.")

# Para iterar una lista integrandola con else, si hay un break no se ejecuta el else.
# for num in nums:
#     print(f"Num: {num}.")
#     # break
# else:
#     print("Termino el for.")

dict = {
    "name": "Andres",
    "lastname": "Ramirez"
}

# Para iterar dict, para obtener keys.
# for key in dict:
#     print(f"Key: {key}.")

# Para iterar dict with items(), para obtener keys and values.
# for key, value in dict.items():
#     print(f"Key: {key}, value: {value}.")

# Para iterar y saltar una iteración with continue.
# for num in nums:
#     if num == 2:
#         continue # para saltar la iteración.
#     print(f"Num: {num}.")

# Para iterar y terminar el bucle with break, el else no se ejecuta si hay break.
# for num in nums:
#     if num == 2:
#         break # para terminar el bucle.
#     print(f"Num: {num}.")
# else:
#     print("Termino el bucle.")

# Para iterar string.
# for caracter in "Hello World...":
#     print(f"Caracter: {caracter}.")

# For en una sola línea, para acciones muy sencillas.
num_por_dos = [num * 2 for num in nums]
print(num_por_dos)