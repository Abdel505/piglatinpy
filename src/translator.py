import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.error import PigLatinError  # Import the custom exception class for handling specific errors.

vowels ="aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
puncuations = ".,:;!?"

class PigLatinTranslator:  # Defines the class for translating phrases to Pig Latin.

    def __init__(self, phrase: str):  # The constructor method to initialize a new translator object.
        self.phrase = phrase  # Stores the input phrase as an instance variable.

    def get_phrase(self) -> str:  # Method to retrieve the original phrase.
        return self.phrase  # Returns the stored phrase.

    def translate(self) -> str:  # Method to translate the phrase into Pig Latin.
        if not self.phrase:
            return "Nil"
        
        translated_phrase = ""
        word = ""


        for i,char in enumerate(self.phrase):
            if char == " " or char == "-" or char in puncuations:
                translated_phrase += PigLatinTranslator.translated_word(word) + char
                word = ""
            elif i == len(self.phrase)-1:
                word += char
                translated_phrase += PigLatinTranslator.translated_word(word)
            else: word += char
        return translated_phrase

    @staticmethod
    def translated_word(word):
       
        if not word:
            return ""

        is_title = word.istitle()
        is_upper = word.isupper()

        lower_word = word.lower()
        first_character = lower_word[0]

        translated = ""
        if first_character in vowels:
            translated = PigLatinTranslator.translate_word_start_with_vowel(lower_word)
        elif first_character in consonants:
            translated = PigLatinTranslator.translate_word_start_with_consonant(lower_word)

        if is_upper:
            return translated.upper()
        elif is_title:
            return translated.title()
        return translated

    @staticmethod
    # First character is a vowel
    def translate_word_start_with_vowel(word):
        last_character = word[-1]
        if last_character == "y":
            return word + "nay"
        elif last_character in vowels:
            return word + "yay"
        else:
            return word + "ay"

    @staticmethod
    # First character is a consonant
    def translate_word_start_with_consonant(word):
        n_cons = 0
        for char in word:
            if char in consonants:
                n_cons +=1
            else:
                break
        
        cons = word[:n_cons]
        rest = word[n_cons:]
        return rest + cons + "ay"


                            

                

            