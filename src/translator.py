from src.error import PigLatinError  # Import the custom exception class for handling specific errors.


class PigLatinTranslator:  # Defines the class for translating phrases to Pig Latin.

    def __init__(self, phrase: str):  # The constructor method to initialize a new translator object.
        self.phrase = phrase  # Stores the input phrase as an instance variable.

    def get_phrase(self) -> str:  # Method to retrieve the original phrase.
        return self.phrase  # Returns the stored phrase.

    def translate(self) -> str:  # Method to translate the phrase into Pig Latin.
        words = self.phrase.split()  # Splits the phrase into a list of individual words.
        translated_words = []  # Initializes an empty list to hold the translated words.
        for word in words:  # Loops through each word from the input phrase.
            if word[0] in "aeiou":  # Checks if the word starts with a vowel.
                translated_words.append(word + "way")  # If it starts with a vowel, adds "way" to the end.
            else:  # If the word starts with a consonant.
                translated_words.append(word[1:] + word[0] + "ay")  # Moves the first letter to the end and adds "ay".
        return " ".join(translated_words)  # Joins the list of translated words back into a single string.
