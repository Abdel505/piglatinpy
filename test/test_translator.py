import sys
import os
from unittest import TestCase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.translator import PigLatinTranslator
from src.error import PigLatinError


class TestPigLatinTranslator(TestCase):

    def test_translate_zabi(self): # Initialize the translator with the phrase "zabi"
        translator = PigLatinTranslator("zabi")
        # Assert that the translation is "abizay"
        self.assertEqual("abizay", translator.translate())


    def test_translate_empty_phrase(self):
        # Initialize the translator with an empty phrase.
        translator = PigLatinTranslator("")
        # Assert that a PigLatinError is raised for an empty phrase.
        with self.assertRaises(PigLatinError):
            translator.translate()
