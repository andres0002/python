# ----------------------------------Exercise 2------------------------------------------

# A) Pedirle al user que diga cualquier text real y:
#   - Calcular cuanto tardaría en decir esa frase.
#   - ¿Cuantas palabras dijo?.

# data.
# Result -> A.
frase = input("Decime una frase y te calculo cuanto tardarías si tuvieras que decirla: ")
count_words = len(frase.split(" "))
print("-------------------------------Start Result A------------------------------------")
print(f"Tardarías en decir esa frase {count_words / 2} segs.")
print(f"Dijiste {count_words} palabras.")
print("-------------------------------End Result A------------------------------------")

# B) Si se tarda más de 1 minuto:
#   - Decirle: "Para flaco tampoco te pedí un testamento.".

# data.
# Parrafo para pasar en la console: La vida está llena de experiencias que nos desafían a ser mejores, a veces en formas inesperadas. Cada etapa de nuestro camino nos brinda oportunidades para aprender lecciones valiosas, aunque muchas veces no nos damos cuenta de su importancia hasta más adelante. Los obstáculos que enfrentamos, por más difíciles que sean, no solo nos ponen a prueba, sino que también nos permiten descubrir nuestras propias fortalezas y capacidades. En este proceso, la resiliencia juega un papel fundamental, ya que nos permite adaptarnos a situaciones complicadas y seguir adelante con la frente en alto. Sin embargo, no estamos solos en este viaje: el apoyo de nuestros amigos, familiares y seres queridos puede marcar la diferencia en los momentos de dificultad. Además, cultivar una actitud positiva y mantener la esperanza viva es crucial, pues nos da la fuerza necesaria para perseverar y continuar persiguiendo nuestros sueños, incluso cuando todo parece incierto.
print("-------------------------------Start Result B------------------------------------")
if (count_words / 2 > 60):
    print("Para flaco tampoco te pedí un testamento.")
print("-------------------------------End Result B------------------------------------")

# C) Dalto habla un 30% más rápido:
#   - ¿Cuanto tardaría él en decirlo?.

# data.
print("-------------------------------Start Result C------------------------------------")
print(f"Dalto tardaría en decir esa frase {round(((count_words / 2) - (count_words / 2 * 0.3)), 2)} segs.")
print("-------------------------------End Result C------------------------------------")