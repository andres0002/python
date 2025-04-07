# *args -> Para pasar mas de un param, se toma como tuple.
# def suma(*args):
#     print(type(args)) # (tuple).
#     return sum(args)
# # execute function.
# print(f"Total: {suma(1, 2, 3, 4, 5)}.")

# **kargs -> Para pasar mas de un key=value, se toma como dict.
# def person(**kargs):
#     print(type(kargs)) # (dict).
#     return kargs
# # execute function.
# dict = person(name="Andres", lastname="Ramirez", age=26)
# for key, value in dict.items():
#         print(f"Key: {key}, value: {value}.")

# (params, *args, **kargs) -> Combinando los types de params en una function.
def params_args_kargs(name, lastname, age, *args, **kargs):
    return name, lastname, age, args, kargs
# execute function.
name, lastname, age, tuple, dict = params_args_kargs(
    "Pepe",
    "Perez",
    26,
    1,
    2,
    3,
    dname="Andres",
    dlastname="Ramirez",
    dage=26
)
print(f"Name: {name}.")
print(f"Lastname: {lastname}.")
print(f"Age: {age}.")
print(f"Tuple: {tuple}.")
print(f"Dict: {dict}.")