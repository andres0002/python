# -----------------------------------Problem txt------------------------------------

# Hay tres listas, una con names, la otra con lastnames y la otra con ages, escribir
# los datos de una forma optima con un for en un file ".txt".

# data.
names = ["Andres", "Juan", "Lucas"]
lastnames = ["Ramirez", "Correa", "Dalto"]
ages = [26, 30, 22]

# Registrar esta info en un file .txt de forma optima con un for.
with open("exercises\\files\\txt\\problem_txt.txt", mode="w", encoding="UTF-8") as file:
    file.writelines(["Los datos son:\n"])
    file.writelines(["-------------------------------------------\n"])
    # forma uno.
    # for name, lastname, age in zip(names, lastnames, ages):
    #     file.writelines([f"Name: {name}, lastname: {lastname}, age: {age}.\n"])
    
    # forma dos.
    [file.writelines([f"Name: {name}, lastname: {lastname}, age: {age}.\n"]) for name, lastname, age in zip(names, lastnames, ages)]