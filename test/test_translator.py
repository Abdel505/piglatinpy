import sys
import os
from unittest import TestCase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.translator import PigLatinTranslator
from src.error import PigLatinError




class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self): # Initialize the translator with the phrase "zabi"
        translator = PigLatinTranslator("zabi")
        result = translator.get_phrase()
        self.assertEqual("zabi", result)
        

    def test_translate_empty_phrase(self):
        translator = PigLatinTranslator("")
        result = translator.translate()
        self.assertEqual("Nil", result)
    
    def test_translate_word_start_with_vowel_end_with_y(self):
        translator = PigLatinTranslator("any")
        result = translator.translate()
        self.assertEqual("anynay", result)
        
    def test_translate_word_start_with_vowels_end_with_vowel(self):
        translator = PigLatinTranslator("apple")
        result= translator.translate()
        self.assertEqual("appleyay", result)

    def test_translate_word_start_with_consonant(self):
        translator = PigLatinTranslator("ask")
        result = translator.translate()
        self.assertEqual("askay", result)
    
