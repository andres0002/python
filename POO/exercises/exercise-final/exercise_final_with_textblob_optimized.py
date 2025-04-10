# -------------------------------Final Exercise With TextBlob Optimized------------------------------------

from textblob import TextBlob # type: ignore

class Sentiment:
    def __init__(self, name, color):
        self.name = name
        # "\x1b[1;31m" -> red
        # "\x1b[1;32m" -> green
        # "\x1b[1;33m" ->  yellow
        # "\x1b[1;34m" ->  blue
        # "\x1b[0;37m" ->  white
        self.color = color
    
    def __str__(self):
        # return f"\x1b[1;{self.color}m{self.name}\x1b[0;37m"
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.name)

class SentimentAnalyzer:
    def __init__(self, ranges):
        self.ranges = ranges
    
    def analyze_sentiment(self, text):
        itextblob = TextBlob(text) # sirve en English.
        for range, sentiment in self.ranges:
            if range[0] < itextblob.sentiment.polarity <= range[1]:
                return sentiment
        return Sentiment("Undefined", "34") # else

ranges = {
    ((-1, -0.9), Sentiment("Very Negative", "31")),
    ((-0.8, -0.5), Sentiment("Negative", "31")),
    ((-0.6, -0.1), Sentiment("Something Negative", "31")),
    ((0, 0.1), Sentiment("Neutral", "33")),
    ((0.2, 0.5), Sentiment("Something Positive", "32")),
    ((0.6, 0.8), Sentiment("Positive", "32")),
    ((0.9, 1), Sentiment("Very Positive", "32")),
}

analizator = SentimentAnalyzer(ranges)

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