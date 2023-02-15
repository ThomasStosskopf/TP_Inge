# encoding : utf8

class Animal:
    """
    Animal is defined by 5 parameters:
    species, age, diet, foot, and name. each animal wil be saved in a file.
    """
    def __init__(self, species, age, diet, foot, name):
        """
        method to define animal's parameters
        :param species: string
        :param age: int
        :param diet: string
        :param foot: int
        :param name: string
        """
        self.species = species
        self.age = age
        self.diet = diet
        self.foot = foot
        self.name = name

    def __str__(self):
        """what will be return if we print an animal"""
        return self.species +"/"+str(self.age) +"/"+self.diet +"/"+str(self.foot) +"/"+self.name




