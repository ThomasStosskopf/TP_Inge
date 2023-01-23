# encoding : utf8
"""
Script for training our skills on using class
We can create animals, that are define by their species, diet
Every animal can have a parent and children
"""
from typing import List


class Animal:
    """
    class Animal where we define general stuff about Animal
    """
    def __init__(self, species: str, age: float, diet, mother="Thomas <3") -> None:
        """
        we define here attribute of our animal class
        :param species: the species (str)
        :param age: age of the animal (float)
        :param diet: animal diet (str?)
        """
        self.species: str = species
        self.age: float = age
        self.diet: str = diet
        # self.children: List[str] = []
        self.mother: str = mother
        self.children: List = []
        self.child_objt: List = []
        self.descendent: List = []

    def __str__(self) -> str:
        """if we do a print on animal, it will print some animal's features"""
        return f"Species : {self.species} \n" \
               f"age: {self.age}\n"\
               f"diet: {self.diet}\n"\
               f"Mother: {self.mother}\n"\
               f"Children: {str(self.children)}\n"\
               f"Descendent: {str(self.descendent)}"
               # f"child memory path:  {str(self.child_id)}\n"\

    def add_children(self, child):
        """
        add_children() adds child (of class Animal) to an Animal.
        In this function, child is an object,
        and we put this attribute in our list of children
        We take the attribute name from or object.
        """
        self.children.append(child.name)
        self.child_objt.append(child)
        self.add_mother(child, self)
        # self.add_descendent(child)

    def add_mother(self, child, mommy):
        """add_mother adds a mother to an Animal object.
        for that purpose, we iterate through all
        the children in children list add change
        the name of their attribute mother
        """
        for element in self.children:
            if element == child.name:
                child.mother = mommy.name

    def add_descendent(self):
        """function to add descendent in the list"""
        all_childrens = [child for child in self.child_objt]
        for child in self.child_objt:
            all_childrens.append(child.add_descendent())
        # explode list of lists created by the above loop
        descendent_objct = []
        for child in all_childrens:
            if isinstance(child, List):
                descendent_objct += child
            else:
                descendent_objct.append(child)

        return descendent_objct

    def show_descendent(self):
        """
        method just to add our descend into the
        list self.descendent. We apply the previous
        method in ou list then we run a for loop inside
        to replace all the barbaric object path with
        the attribute name associated with.
        """
        self.descendent = self.add_descendent()
        self.descendent = [child.name for child in self.descendent]
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

    # def retrieve_children(self, input_animal: Animal) -> None:
    #     """ retrieve_children returns all children object into a List"""
    #     children = input_animal.descendent
    #     self.descendent = children


# TEST HERE

if __name__ == "__main__":
    Dog0 = Dog(age=10, name= "Boby")
    Dog1 = Dog(age=8, name="Martel")
    Dog3 = Dog(age=8, name="Hakam")
    Dog4 = Dog(age=7, name="Joelle")
    Dog5 = Dog(age=5, name="Patate")
    Dog0.add_children(Dog3)
    Dog0.add_children(Dog1)
    Dog1.add_children(Dog5)
    # lst = Dog0.add_descendent()  #[0]
    # print(f"my list: {lst}")

    print(Dog0.show_descendent())
    print(Dog0)
    # print(Dog1)
    # print(Dog3)
    # print(Dog5)
    #print(f"my list: {lst}")


    # pouvoir ajouter un enfant dans un animal
    # afficher tous les descendants d'un animal
    # si j'ia un animal qui a un ensemble d'animal comme descendant
    # on veut aussi les descendants de ses descendants
    # l'animal est capable de connaître sa mère
