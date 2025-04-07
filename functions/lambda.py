# lambda -> anonymous function -> structure -> name = lambda *params : action
# , cómo functions flecha en JS.
# Para realizar actions sencillas y rapido.
# No es acta para realizar mas de una action o instrucción.
suma = lambda *args : sum(args)
print(f"Total: {suma(1, 2)}.")

# nums pares con lambda.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
nums_pares = list(filter(lambda num : num % 2 == 0 and num != 0, nums))
print(f"Nums pares: {nums_pares}.")