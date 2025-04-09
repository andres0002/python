# -------------------------------Exercise 1-----------------------------------------

# Crear un juego de fusión:

# El juego consiste en crear personajes y que esos personajes se puedan fusionar
# para formar personajes más poderosos.

# Para ello deberemos cambiar el comportamiento del operator "+" para que cuando
# los personajes se fusionen, salga un new personaje con habilidades mejoradas.

# Una posible fórmula es: El promedio de las habilidades de ambos al cuadrado.

class Character:
    def __init__(self, name, force, speed):
        self.name = name
        self.force = force
        self.speed = speed
    
    def __repr__(self):
        return f"{self.name}(force:{self.force},speed:{self.speed})"
    
    def __add__(self, other_character):
        # concatenar names.
        new_name = self.name + other_character.name
        # promedio al cuadrado
        new_force = round(((self.force + other_character.force)/2)**2)
        # promedio al cuadrado
        new_speed = round(((self.speed + other_character.speed)/2)**2)
        return Character(new_name, new_force, new_speed)

# structure de la list[(id, object)].
list_characters = []

# obtine ya sea la fuerza, velocidad, option que ingrese el user.
def get_force_or_speed_or_option(message):
    while True:
        try:
            value = int(input(message))
            break
        except:
            print(" -----------------Debe ingresar un num de type int----------------")
    return value

# para crear el personaje.
def create_character():
    name = input("Ingrese el name del character: ")
    force = get_force_or_speed_or_option("Ingrese la force del character: ")
    speed = get_force_or_speed_or_option("Ingrese la speed del character: ")
    character = Character(name, force, speed)
    return character

# muestra los personajes.
def show_characters():
    print("----------------------------------Start Show Characters----------------------------------")
    for id_character, character in list_characters:
        print(f"Character -> ID: {id_character}, name: {character.name}, force: {character.force}, spped: {character.speed}.")
    print(" ----------------------------------End Show Characters-----------------------------------")

# obtiene un personaje por id.
def get_character_by_id(id):
    for id_character, character in list_characters:
        if id_character == id:
            finded_character = character
            return finded_character
    return ValueError

# valida que el personaje exista en la list y si existe lo retorna.
def id_is_exist(message):
    while True:
        try:
            id = int(input(message))
            if get_character_by_id(id) == ValueError:
                raise ValueError
            finded_character = get_character_by_id(id)
            break
        except:
            print(" -----------------Debe digitar un ID existente y que sea de type int----------------")
    return finded_character

# fusiona los personajes, y crea un personaje nuevo resultante de la fusión.
def merge_characters():
    create_character1 = id_is_exist("Digite el ID del primer personaje a fusionar: ")
    create_character2 = id_is_exist("Digite el ID del segundo personaje a fusionar: ")
    merged_character = create_character1 + create_character2
    list_characters.append((len(list_characters), merged_character))

# method main.
if __name__ == '__main__':
    print("--------------------------Started play----------------------------") 
    while True:
        print(" ----------------------------Options-----------------------------")
        print("1. Create character.")
        print("2. Merge characters.")
        print("3. Show character.")
        print("4. Exit play.")
        option = get_force_or_speed_or_option("Digite la option: ")
        if option == 1:
            list_characters.append((len(list_characters), create_character()))
        elif option == 2:
            if len(list_characters) < 2:
                show_characters()
                print("Debe tener por lo menos dos personajes registrados en el juego.")
            else:
                show_characters()
                merge_characters()
                show_characters()
        elif option == 3:
            show_characters()
        elif option == 4:
            break
        else:
            print("-----------------Debe digitar una option valida------------------")
    print("---------------------------Ended play-----------------------------")