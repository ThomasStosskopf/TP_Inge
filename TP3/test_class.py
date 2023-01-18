"""
Script to
"""
class Animal():
    def __init__(self, species, age, diet) -> None:
        self.species = species
        self.age = age
        self.diet = diet
        self.foot = 2

    def set_species(self, species):
        self.species = species

    def set_foot_nb(self, foot) :
        self.foot = foot

    def set_age(self, age):
        self.age = age

    def set_diet(self, diet):
        self.diet = diet

    def __str__(self) -> str:
        return self.species + " " + str(self.age) + " " + self.diet + " " + str(self.foot)

class Homme(Animal):
    def __init__(self, age , name) -> None:
        print("[Homme.__init] " + name)
        super().__init__("homme", age, "Omnivore")
        self.age = age
        self.name = name

    def __str__(self):
        return super().__str__() + "\nname : " + self.name


class Snake(Animal) :
    def set_foot_nb(self, foot) :
        self.foot = 0

if __name__ == "__main__":
    animal0 = Animal("chien", 10 , "carnivore")
    animal1 = Animal("chien", 10 , "carnivore")
    # animal1.set_species("chien")
    # animal1.set_age(10)
    # animal1.set_diet("carnivore")

    animal2 = Homme(40, "Jacque")
    animal3 = Snake("Snake", 5, "Carnivore")
    animal3.set_foot_nb(10)
    animal2.set_foot_nb(2)
    # print(animal0)
    # print(animal1)
    print(animal2)
    # print(animal3)


    # pouvoir ajouter un enfant dans un animal
    # afficher tous les descendants d'un animal
    # si j'ia un animal qui a un ensemble d'animal comme descendant
    # on veut aussi les descendants de ses descendants
    # l'animal est capable de connaître sa mère