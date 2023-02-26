# encoding : utf8
import unittest
from model import Model
from animal import Animal
"""
Script to test the function of model.py
"""

class Test_model(unittest.TestCase):
    """test case to test functions from model.py"""
    def setUp(self):
        """Setup a new Model instance and a new Animal instance"""
        self.model = Model("test_file.txt")
        self.animal = Animal("Dog", "5", "Carnivore", "4", "Fido")

    def test_init(self):
        """Test that the Model instance is initialized correctly"""
        self.assertEqual(self.model.filename, "test_file.txt")
        self.assertEqual(self.model.file.mode, "r+")
        self.assertIsInstance(self.model.dico_animaux, dict)


