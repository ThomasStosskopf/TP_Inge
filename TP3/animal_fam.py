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
    def __init__(self, species, age, diet, mother = "Thomas <3") -> None:
        """
        we define here attribute of our animal class
        :param species: the species
        :param age: age of the animal
        :param diet: animal diet
        """
        self.species = species
        self.age = age
        self.diet = diet
        self.children = [None]
        self.mother = mother
        # a list of the id of the variable in memory
        self.child_id = []
        self.descendent = [None]

    def __str__(self) -> str:
        """if we do a print on animal, it will print some animal's features"""
        return "Species : " + self.species + "\n" \
            +"age : " + str(self.age) + "\n" \
            +"diet : "+ self.diet + "\n"\
            +"Mother : " + self.mother + "\n"\
            + "Children : " + str(self.children) + "\n"\
            + "child memory path : " + str(self.child_id) +"\n"\
            + "Descendent : " + str(self.descendent)

    def add_children(self, child):
        """function to add child to an animal"""
        # In this function, child is an object,
        # We take the attribute name from or object
        # and we put this attribute in our list of children
        if self.children[0] is None:
            self.children.remove(None)
        self.children.append(child.name)
        self.child_id.append(id(child))
        self.add_mother(child,self)
        self.add_descendent()

    def add_mother(self,child ,mommy):
        """function to add a mother
        for that purpose, we iterate through all
        the children in children list add change
        the name of their attribute mother
        """
        for element in self.children:
            if element == child.name:
                child.mother = mommy.name

    def add_descendent(self):
        """function to add descendent in the list"""
        for elem in self.child_id:
            for kids in self.children:
                self.descendent.append(kids)

        return self.descendent






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



class Dog(Animal):
    """Dog class to define a new species : dog"""
    def __init__(self, age, name) -> None:
        """function to init a dog with default features"""
        super().__init__("Dog", age, "carnivore")
        self.age = age
        self.name = name
        self.foot = 4

    def __str__(self):
        """function to print features form Animal() and from Dog()"""
        return "______________________\n" \
            + "\nname : " + self.name +"\n"+\
            "______________________\n"+ super().__str__()

# TEST HERE TO ADD WITHOUT PASSWOD

if __name__ == "__main__":
    Dog0 = Dog(10, "Boby")
    Dog1 = Dog(8, "Martel")
    Dog3 = Dog(8, "Hakam")
    Dog4 = Dog(7, "Joelle")
    Dog5 = Dog(5, "Patate")
    Dog0.add_children(Dog3)
    Dog0.add_children(Dog1)
    Dog1.add_children(Dog5)
    print(Dog0.add_descendent())
    print(Dog1)
    print(Dog3)
    print(Dog5)




    # pouvoir ajouter un enfant dans un animal
    # afficher tous les descendants d'un animal
    # si j'ia un animal qui a un ensemble d'animal comme descendant
    # on veut aussi les descendants de ses descendants
    # l'animal est capable de connaître sa mère