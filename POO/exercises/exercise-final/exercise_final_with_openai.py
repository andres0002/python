# -------------------------------Final Exercise With OpenAI------------------------------------

# Chatbot analizador de sentimientos.

# En este proyecto, podrías desarrollar un chatbot en python, que nos pida
# que le digamos algo y tome eso que le decimos, analice el sentimiento
# y nos responda cual es el sentimiento.

# Este proyecto te daría la oportunidad de trabajar con varios conceptos de la
# Programacción Orientada a Objetos (POO), módulos, API's, análisis de datos, etc...

import openai # type: ignore

openai.api_key = "api-key"
system_rol = """
    Hace de cuenta que sos un analizador de sentimientos.
    Yo te paso sentimientos y vos analizas el sentimiento de los mensajes
    y me das una respuesta con almenos 1 caracter y como máximo 4 caracteres
    SOLO RESPUESTAS NUMÉRICAS.
    Donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima.
    (Podes responder solo con ints o floats).
"""

# system -> Cómo se debe comportar el sistema.
messages = [{"role": "system", "content": system_rol}]

class SentimentAnalyzer:
    def analyze_sentiment(self, polarity):
        if polarity >= -1 and polarity <= -0.9:
            # 31 -> para darle color al text o console -> red.
            return "\x1b[1;31m" + "Very Negative." + "\x1b[0;37m"
        elif polarity >= -0.8 and polarity <= -0.5:
            return "\x1b[1;31m" + "Negative." + "\x1b[0;37m"
        elif polarity > -0.5 and polarity < -0.1:
            return "\x1b[1;31m" + "Something Negative." + "\x1b[0;37m"
        elif polarity >= -0.1 and polarity <= 0.1:
            return "\x1b[1;33m" + "Neutral." + "\x1b[0;37m"
        elif polarity > 0.1 and polarity <= 0.5:
            return "\x1b[1;32m" + "Something Positive." + "\x1b[0;37m"
        elif polarity > 0.5 and polarity <= 0.8:
            return "\x1b[1;32m" + "Positive." + "\x1b[0;37m"
        elif polarity > 0.9 and polarity <= 1:
            return "\x1b[1;32m" + "Very Positive." + "\x1b[0;37m"
        else:
            return "\x1b[1;34m" + "Undefined." + "\x1b[0;37m"

analizator = SentimentAnalyzer()

print(f"Result de analisis: {analizator.analyze_sentiment(-1)}.")
print(f"Result de analisis: {analizator.analyze_sentiment(-0.8)}.")
print(f"Result de analisis: {analizator.analyze_sentiment(-0.4)}.")
print(f"Result de analisis: {analizator.analyze_sentiment(-0.1)}.")
print(f"Result de analisis: {analizator.analyze_sentiment(0.2)}.")
print(f"Result de analisis: {analizator.analyze_sentiment(0.6)}.")
print(f"Result de analisis: {analizator.analyze_sentiment(1)}.")
print(f"Result de analisis: {analizator.analyze_sentiment(4)}.")

while True:
    user_prompt = input("\x1b[1;33m" + "\nDecime algo: " + "\x1b[0;37m")
    # user -> Cómo se debe comportar el user.
    messages.append({"role": "user", "content": user_prompt})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        max_token = 8
    )
    
    # assistant -> como se debe compartar el asistente o chetgpt.
    response = completion.choices[0].message["content"]
    messages.append({"role": "assistant", "content": response})
    
    print(f"Result sentimiento is: {analizator.analyze_sentiment(float(response))}")
    
    num = int(input("Si quieres finalizar digita -> 1."))
    if num == 1:
        break

# Hello, I'm very good.
# Hello, I'm good.
# The book is on the table.
# It's a day like any other.
# Hello, I'm very bad.
# Hello, I'm not very feel.
# Hello, I'm bad.

# "\x1b[1;31m" -> red
# "\x1b[1;32m" -> green
# "\x1b[1;33m" ->  yellow
# "\x1b[1;34m" ->  blue
# "\x1b[0;37m" ->  white