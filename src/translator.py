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
        word = self.phrase
        for char in word:
            first_character = word[0]
            last_character = word[-1]
            if first_character in vowels:
                if last_character == "y":
                    return word + "nay"
                elif last_character in vowels:
                    return word + "yay"
                else:
                    return word + "ay"
            if first_character in consonants:
                return word[1:] + word[:1] + "ay"
                #return word[1:]
            