# encoding : utf8
"""controller for our graphic interface"""
from vue import Application
from model import Model

class Controller:
    """controller class, will be used to interact between
    vue.py and model.py
    the controller will do every actions.
    """
    def __init__(self):
        """init our controller"""
        self.model = Model("a.txt") # define where we are going to write and seek for animal
        self.model.read_file() # read the previous file in Model
        self.view = Application(self)

        self.view.view_window()  # call the method from vue.py

    def display(self, value):
        """method to display an animal on the window"""
        self.view.display_label(self.model.dico_animaux[value])

    def add_animal(self, dict_animal):
        """Method to save an animal in our dict"""
        self.model.save(dict_animal)

    def get_model_entries(self):
        return self.model.get_attributes()

    def quit_window(self):
        """
        method to quit the window
        """
        print("close app")
        self.model.close()
        self.view.destroy()


if __name__ == "__main__":
    C = Controller()





# prochaine fois
# faire en sorte que l'on affiche toute la liste de tous les animaux
# du fichier a.txt, et que l'on puisse ajouter un animal, ou modifier un animal
# quand on supprimer on doit pouvoir supprimer sur la bonne ligne du fichier
# quand on add remise à zéro des champs








