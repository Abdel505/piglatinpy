import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.error import PigLatinError  # Import the custom exception class for handling specific errors.

vowels ="aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

class PigLatinTranslator:  # Defines the class for translating phrases to Pig Latin.

    def __init__(self, phrase: str):  # The constructor method to initialize a new translator object.
        self.phrase = phrase  # Stores the input phrase as an instance variable.

    def get_phrase(self) -> str:  # Method to retrieve the original phrase.
        return self.phrase  # Returns the stored phrase.

    def translate(self) -> str:  # Method to translate the phrase into Pig Latin.
        if not self.phrase:
            return "Nil"
        
        words = self.phrase.split()
        translated_words = []

        for word in words:
            if not word:
                continue

            first_character = word[0]
            last_character = word[-1]

            if first_character in vowels:
                if last_character == "y":
                    translated_words.append(word + "nay")
                elif last_character in vowels:
                    translated_words.append(word + "yay")
                else:
                    translated_words.append(word + "ay")
            elif first_character in consonants:
                translated_words.append(self.handle_consonants(word))
            else:
                translated_words.append(word)

        return " ".join(translated_words)

    def handle_consonants(self, word: str) -> str:
        n_cons = 0
        for char in word:
            if char in consonants:
                n_cons += 1
            elif char in vowels:
                break
        cons = word[:n_cons]
        rest = word[n_cons:]
        return rest + cons + "ay"

                            

                

            