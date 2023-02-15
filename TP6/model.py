# encoding : utf8
"""model """
from animal import Animal

class Model:
    """
    Model to save animal in a file, and give it to the controller
    """
    def __init__(self, filename):
        """init class Model
        with filename as the file we are going to use.
        """
        self.filename = filename
        self.file=open(self.filename, "r+", encoding='utf-8') # r+ = read + write
        self.dico_animaux = {}

    def read_file(self):
        """
        method to read all animal in our file
        """
        for line in self.file:
            line = line.strip()
            tab = line.split(",")
            a = Animal(tab[0], tab[1], tab[2], tab[3], tab[4])
            self.dico_animaux[a.name] = a

    def save(self, dict_animal):
        """
        method to save animal in the file a.txt
        """
        self.file.write("\n" + dict_animal["species"] + ","
                        + dict_animal["age"] + "," + dict_animal["diet"]
                        + "," + dict_animal["foot"]
                        + "," + dict_animal["name"])

    def close(self):
        """
        method to close the file
        """
        self.file.close()

    def get_attributes(self) -> []:
        """method to get the attributes of the class Animal"""
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

if __name__ == "__main__" :
    model = Model("a.txt")
    model.read_file()
    model.close()
