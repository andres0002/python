# -------------------------------Final Exercise With TextBlob------------------------------------

# Chatbot analizador de sentimientos.

# En este proyecto, podrías desarrollar un chatbot en python, que nos pida
# que le digamos algo y tome eso que le decimos, analice el sentimiento
# y nos responda cual es el sentimiento.

# Este proyecto te daría la oportunidad de trabajar con varios conceptos de la
# Programacción Orientada a Objetos (POO), módulos, API's, análisis de datos, etc...

from textblob import TextBlob # type: ignore

class SentimentAnalyzer:
    def analyze_sentiment(self, text):
        analysis = TextBlob(text) # sirve en English.
        if analysis.sentiment.polarity > 0:
            return "\x1b[1;32m" + "Positive" + "\x1b[0;37m"
        elif analysis.sentiment.polarity == 0:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "Negative" + "\x1b[0;37m"

analizator = SentimentAnalyzer()

while True:
    user_prompt = input("\x1b[1;33m" + "\nDecime algo: " + "\x1b[0;37m")
    
    print(f"Result sentimiento is: {analizator.analyze_sentiment(user_prompt)}")
    
    num = int(input("Si quieres finalizar digita -> 1, si no -> 0: "))
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