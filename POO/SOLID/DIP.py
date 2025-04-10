# DIP -> Dependency Inversion Principle -> Principio de Inversión de Dependencia, Se debe depender de abstracciones,
# no de implementaciones concretas.

from abc import ABC, abstractmethod

# no cumple con el principio.
class Dictionary:
    def verify_word(self, word):
        # implementation.
        pass

class CheckerSpelling:
    def __init__(self):
        self.dictionary = Dictionary()
    
    def correct_text(self, text):
        # implementation -> use -> dictionary.
        pass

checker_spelling = CheckerSpelling()

# cumple con el principio
class VerifySpelling(ABC):
    @abstractmethod
    def verify_word(self, word):
        # implementation.
        pass

class Dictionary(VerifySpelling):
    def verify_word(self, word):
        # implementation -> use -> dictionary.
        pass

class ServiceOnline(VerifySpelling):
    def verify_word(self, word):
        # implementation -> use -> serviceOnline.
        pass

class CheckerSpelling:
    def __init__(self, checker):
        self.checker = checker
    
    def correct_text(self, text):
        # implementation -> use -> dictionary or serviceOnline.
        pass

checker_spelling = CheckerSpelling(Dictionary())
checker_spelling = CheckerSpelling(ServiceOnline())