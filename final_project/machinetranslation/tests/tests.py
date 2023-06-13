import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))

from machinetranslation.translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hi'), 'Bonjour') # test when bread is given as input the output is pain.
        self.assertEqual(english_to_french('bread'), 'pain') # test when bread is given as input the output is pain.
        self.assertEqual(english_to_french('water'), 'eau') # test when water is given as input the output is eau.

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when Bonjour. is given as input the output is Hello 
        self.assertEqual(french_to_english('pain'), 'bread') # test when pain is given as input the output is bread.
        self.assertEqual(french_to_english('eau'), 'water') # test when eau is given as input the output is water.

        
unittest.main()
