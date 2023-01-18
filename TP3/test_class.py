"""
Script to train class
"""
class Animal():
    """
    class animal where we define general stuff about animal
    """
    def __init__(self, species, age, diet) -> None:
        """
        we define here attribute of our animal class
        :param species: the species
        :param age: age of the animal
        :param diet: animal diet
        """
        self.species = species
        self.age = age
        self.diet = diet
        self.foot = 2



    def __str__(self) -> str:
        """if we do a print on animal, it will print this"""
        return self.species + " " + str(self.age) + " " + self.diet + " " + str(self.foot)

class Homme(Animal):
    """class for the species Homme"""
    def __init__(self, age , name) -> None:
        """init what homme is, it is always 'homme' and 'omnivore" """
        super().__init__("homme", age, "Omnivore")
        self.age = age
        self.name = name

    def __str__(self):
        return super().__str__() + "\nname : " + self.name


class Snake(Animal):
    """class for the species snake"""
    def set_foot_nb(self, foot) :
        self.foot = 0

if __name__ == "__main__":
    animal0 = Animal("chien", 10 , "carnivore")
    animal1 = Animal("chien", 10 , "carnivore")



    # pouvoir ajouter un enfant dans un animal
    # afficher tous les descendants d'un animal
    # si j'ia un animal qui a un ensemble d'animal comme descendant
    # on veut aussi les descendants de ses descendants
    # l'animal est capable de connaître sa mère