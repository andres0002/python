# snake_case -> Palabras separadas por "_" -> "word1_word2".
# camelCase -> Para que la primera palabra tenga el primer caracter en minuscula
# y las siguientes palabras el primer caracter en mayuscula -> "word1Word2".
# PascalCase -> Para que el primer caracter de cada palabra sea mayuscula ->
# "Word1Word2".

# class -> Palabra clave para definir un clase.

class Celular(): # Class -> # () -> Se utiliza para herencia de clases.
    # attributes static.
    mark = "Samsung"
    model = "S23"
    camera = "48MP"
    
cel1 = Celular() # cel1 -> object -> instacia de una class.

print(f"Mark: {cel1.mark}, model: {cel1.model}, camera: {cel1.camera}.")