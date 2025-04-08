def suma(num1, num2):
    return num1 + num2

while True:
    try:
        num1 = int(input("Ingresa el primer num: "))
        num2 = int(input("Ingresa el segundo num: "))
        print(f"Suma igual a: {suma(num1, num2)}")
    except (
            # BaseException es la base común de todas las excepciones
            BaseException,
            # Exception es la base de todas las excepciones no fatales.
            Exception,
            # ZeroDivisionError: Se lanza cuando se intenta dividir por cero.
            ZeroDivisionError,
            # NameError: Ocurre cuando se intenta acceder a una variable que no ha sido definida.
            NameError,
            # TypeError: Se genera cuando se intenta realizar una operación no válida entre tipos de datos incompatibles.
            TypeError,
            # ValueError: Ocurre cuando una operación o función recibe un argumento del tipo correcto pero con un valor inapropiado.
            ValueError,
            # IndexError: Se produce cuando se intenta acceder a un índice de una secuencia que está fuera de rango.
            IndexError,
            # KeyError: Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
            KeyError,
            # OSError: Se lanza cuando un comando de I/O falla o se produce un error relacionado con el sistema operativo.
            OSError,
            # SystemError se lanza cuando se produce un error del sistema que no puede ser manejado por el intérprete de Python.
            SystemError
        ):
        print(f"Error: {ValueError}.")
        print("Ambos nums a sumar deben ser de type int.")
    else:
        break
    finally:
        print("Finally...")