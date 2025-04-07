with open("files\\file.txt", mode="w", encoding="UTF-8") as file:
    print("Ok...")
    
    # para sobre escribir en el file.
    # file.write("XD")
    
    # para escribir las lineas, y sobre escribe el file si tenia algo antes de abrirlo.
    file.writelines(["Line 1.\n", "Line 2.\n", "Line 3.\n"])
    file.writelines(["Line 4.\n", "Line 5.\n", "Line 6."])