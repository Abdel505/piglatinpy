import sys
import os
from unittest import TestCase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.translator import PigLatinTranslator
from src.error import PigLatinError




class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self): # Initialize the translator with the phrase "zabi"
        translator = PigLatinTranslator("abdel_505")
        result = translator.get_phrase()
        self.assertEqual("abdel_505", result)
        

    def test_translate_empty_phrase(self):
        translator = PigLatinTranslator("")
        result = translator.translate()
        self.assertEqual("Nil", result)
    #Words Start with Vowel
    def test_translate_word_start_with_vowel_end_with_y(self):
        translator = PigLatinTranslator("any")
        result = translator.translate()
        self.assertEqual("anynay", result)
        
    def test_translate_word_start_with_vowels_end_with_vowel(self):
        translator = PigLatinTranslator("apple")
        result= translator.translate()
        self.assertEqual("appleyay", result)

    def test_translate_word_start_with_vowels_and_end_with_consonant(self):
        translator = PigLatinTranslator("ask")
        result = translator.translate()
        self.assertEqual("askay", result)
    #Words Start with Consoneent
    def test_translate_word_start_with_more_consonents(self):
        translator = PigLatinTranslator("hhello")
        result = translator.translate()
        self.assertEqual("ellohhay", result)
    def test_translate_phrase_contain_space_hypen_pounctuation(self):
        translator = PigLatinTranslator("hello-World yes-ask")
        result= translator.translate()
        self.assertEqual("ellohay-Orldway esyay-askay", result)
    def test_traslate_uapper_case_word(self):
        translator = PigLatinTranslator("HELLO")
        result = translator.translate()
        self.assertEqual("ELLOHAY", result)
    def test_traslate_tittle_case_word(self):
        translator = PigLatinTranslator("Hello")
        result = translator.translate()
        self.assertEqual("Ellohay", result)
    # This test whene translated_word method is called with an empty string
    def test_translate_phrase_with_multihypen(self):
        translator = PigLatinTranslator("hello--ask")
        result = translator.translate()
        self.assertEqual("ellohay--askay", result)
    
    