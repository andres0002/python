# ------------------------------------Exercise 3----------------------------------

# Create una function que nos devuelva la serie fibonacci entre 0 y el num dado.

def fibonacci(num):
    a, b = 0, 1
    list_fibonacci = [0]
    for i in range(num):
        if b > num:
            return list_fibonacci
        else:
            list_fibonacci.append(b)
            a, b = b, a + b

print(fibonacci(34))