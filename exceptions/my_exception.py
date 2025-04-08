class MyException(Exception):
    def __init__(self, error):
        print(f"Error: {error}.")

# raise -> Para lanzar exceptions.

# No se maneja la exception.
# raise MyException("XD")

# Manejado la exception.
try:
    raise MyException("XD")
except:
    print("XD")