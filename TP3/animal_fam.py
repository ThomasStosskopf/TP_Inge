# encoding : utf8
"""
Script for training our skills on using class
We can create animals, that are define by their species, diet
Every animal can have a parent and children
"""
import gc
from typing import List, Dict


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
        self.children: List[str] = []
        self.mother: str = mother
        self.child_id: List = []
        """child_id is a list of the id of the variable in memory"""
        self.descendent: List = []

    def __str__(self) -> str:
        """if we do a print on animal, it will print some animal's features"""
        return f"Species : {self.species} \n" \
               f"age: {self.age}\n"\
               f"diet: {self.diet}\n"\
               f"Mother: {self.mother}\n"\
               f"Children: {str(self.children)}\n"\
               f"child memory path:  {str(self.child_id)}\n"\
               f"Descendent: {str(self.descendent)}"

    def add_children(self, child):
        """
        add_children() adds child (of class Animal) to an Animal.
        In this function, child is an object,
        and we put this attribute in our list of children
        We take the attribute name from or object.
        """
        self.children.append(child.name)
        self.child_id.append(child)
        self.add_mother(child,self)
        self.add_descendent(child)

    def add_mother(self, child, mommy):
        """add_mother adds a mother to an Animal object.
        for that purpose, we iterate through all
        the children in children list add change
        the name of their attribute mother
        """
        for element in self.children:
            if element == child.name:
                child.mother = mommy.name

    def add_descendent(self, child):
        """function to add descendent in the list"""


        for index in range(len(self.child_id)):
            self.descendent.append(self.children[index])
            self.descendent.append(child.add_descendent(child))
        return self.descendent

    # def retrieve_children(self, input_animal) -> None:
    #     """ retrieve_children returns all children object into a List"""
    #     descendent = []
    #     children = input_animal.descendent
    #     for child in children:
    #         pass
    #         # descendent.append(child.)
    #     flag = True
    #     while flag:
    #         for child in children:
    #             descendent.append(child)
    #     # animal -> [child1,child2]
    #     #     -> child1 -> [child12, child13]
    #     for child in children:
    #         descendent.append(child)
    #         foobar = child.descendent
    #         while len(foobar) < 1:
    #             descendent.append(*child.descendent)
    #             pass # foobar[:]


    # def get_children(self):
    #     return self.descendent
    #
    # def get_descendence_list(self, animal):
    #     first_level_children = animal.descendent
    #     children_list = [first_level_children]
    #     while len(children_list)>1:
    #         children_list.append(*self.get_descendence_list(animal))
    #         pass # first_level_children
    #     return children_list
# Function for nth Fibonacci number


# Driver Program
# print(Fibonacci(9))

# This code is contributed by Saket Modi
# then corrected and improved by Himanshu Kanojiya

 # """
 #        Recursively adds all descendants of the animal to a list
 #        """
 #        descendants = []
 #        for child_id in self.child_id:
 #            child = None
 #            for obj in gc.get_objects():
 #                if id(obj) == child_id:
 #                    child = obj
 #                    break
 #            if child is None:
 #                continue
 #            descendants.append(child)
 #            descendants.extend(child.add_descendents())
 #        return descendants













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
    Dog0 = Dog(age=10,name= "Boby")
    Dog1 = Dog(age=8, name="Martel")
    Dog3 = Dog(age=8, name="Hakam")
    Dog4 = Dog(age=7, name="Joelle")
    Dog5 = Dog(age=5, name="Patate")
    Dog0.add_children(Dog3)
    Dog0.add_children(Dog1)
    Dog1.add_children(Dog5)
    print(Dog0)
    print(Dog1)
    print(Dog3)
    print(Dog5)

    # bob = {
    #     'mother': ['thomas'],
    #     'child': []
    # }
    #
    # francis = {
    #     'mother': ['thomas'],
    #     'child': [bob]
    # }
    #
    # lucas = {
    #     'mother': ['thomas'],
    #     'child': [francis]
    # }

    # def return_all_fib(n=15):
    #     def Fibonacci(n):
    #         # Check if input is 0 then it will print incorrect input
    #         if n < 0:
    #             print("Incorrect input")
    #         # Check if n is 0 then it will return 0
    #         elif n == 0:
    #             return 0
    #         # Check if n is 1,2 it will return 1
    #         elif n == 1 or n == 2:
    #             return 1
    #         else:
    #             return Fibonacci(n - 1) + Fibonacci(n - 2)
    #     return [Fibonacci()]

    # def get_child(dog: Dict):
    #     if dog['child']
    #     return dog['child']
    # dogs = []
    # while new_children is not None:
    #     dogs.append()
    #     new_children = get_child(child)
    #     return [dog.get_children()]
    # def get_child(dog):
    #         return []
    #     else


    # pouvoir ajouter un enfant dans un animal
    # afficher tous les descendants d'un animal
    # si j'ia un animal qui a un ensemble d'animal comme descendant
    # on veut aussi les descendants de ses descendants
    # l'animal est capable de connaître sa mère
