# open file para poderlo trabajar.
with open("files\\file.txt") as file:
    print("Ok...")
    
    # leer txt.
    # print(file.read())
    
    # leer lineas del txt.
    # print(file.readlines())
    
    # leer una sola linea del txt.
    print(file.readline())
    
    # no es necesario cerralo al usar with open.