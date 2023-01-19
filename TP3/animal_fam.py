# encoding : utf8
"""
Script for training our skills on using class
We can create animals, that are define by their species, diet
Every animal can have a parent and children
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
        self.children = [None]
        self.mother = "Thomas <3"

    def __str__(self) -> str:
        """if we do a print on animal, it will print some animal's features"""
        return "Species : " + self.species + "\n" \
            +"age : " + str(self.age) + "\n" \
            +"diet : "+ self.diet + "\n"\
            +"Foot : "+ str(self.foot) + "\n"\
            +"Mother : " + self.mother + "\n"\
            + "Children : " + str(self.children)

    def add_children(self, child):
        """function to add child to an animal"""
        if self.children[0] is None:
            self.children.remove(None)
        return self.children.append(child)


class Homme(Animal):
    """class for the species Homme"""
    def __init__(self, age , name) -> None:
        """init what homme is, it is always 'homme' and 'omnivore" """
        super().__init__("homme", age, "Omnivore")
        self.age = age
        self.name = name

    def __str__(self):
        """function to print info form Animal() and from Homme()"""
        return super().__str__() + "\nname : " + self.name

class Snake(Animal):
    """class for the species snake"""
    def set_foot_nb(self) :
        """function to default set Snake foot to 0"""
        self.foot = 0

class Dog(Animal):
    """Dog class to define a new species : dog"""
    def __init__(self, age, name) -> None:
        """function to init a dog with default parameters"""
        super().__init__("Dog", age, "carnivore")
        self.age = age
        self.name = name
        self.foot = 4

    def __str__(self):
        """function to print features form Animal() and from Dog()"""
        return "______________________\n" \
            + "\nname : " + self.name +"\n"+\
            "______________________\n"+ super().__str__()

if __name__ == "__main__":
    animal0 = Dog(10, "Boby")
    animal1 = Dog(1, "Martel")
    animal1.add_children("Boby")
    print(animal1)


    # pouvoir ajouter un enfant dans un animal
    # afficher tous les descendants d'un animal
    # si j'ia un animal qui a un ensemble d'animal comme descendant
    # on veut aussi les descendants de ses descendants
    # l'animal est capable de connaître sa mère
