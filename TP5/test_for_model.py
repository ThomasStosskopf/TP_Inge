# encoding : utf8
"""
Script to test the function of model.py
"""
import unittest
from model import Model
from animal import Animal


class Testmodel(unittest.TestCase):
    """test case to test functions from model.py"""
    def setUp(self):
        """Setup a new Model instance and a new Animal instance"""
        self.model = Model("test_file.txt")
        self.animal = Animal("Koala", "5", "Carnivore", "4", "Martel")

    def test_init(self):
        """Test that the Model instance is initialized correctly"""
        self.assertEqual(self.model.filename, "test_file.txt")
        self.assertEqual(self.model.file.mode, "r+")
        self.assertIsInstance(self.model.dico_animaux, dict)

    def test_save(self):
        """Test that the Model instance can save an animal to a file"""
        # Save the animal to the file
        self.model.save(self.animal.__dict__)
        # Read the animal from the file
        self.model.read_file()
        # Check that the animal was saved correctly
        self.assertEqual(self.model.dico_animaux["Martel"].species, "Koala")

    def test_delete_animal(self):
        """Test that the Model instance can delete an animal from a file"""
        # Add an animal that we will delete
        temp_animal = {"species":"Dog", "age":"5","diet": "Carnivore", "foot": "5", "name": "Fido"}
        self.model.save(temp_animal)
        # Delete the animal from the file
        self.model.delete_animal("Fido")
        # Read the file and the dictionary
        self.model.read_file()
        dico_animaux = self.model.dico_animaux
        # Check that the animal was deleted from the file
        self.assertNotIn("Fido", dico_animaux)
