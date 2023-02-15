# encoding : utf8
"""controler for our graphic interface"""
from vue import Application
from model import Model

class Controller:
    def __init__(self):
        """init our controller"""
        self.view = Application(self)
        self.model = Model("a.txt")

        self.view.view_window()  # call the method from vue.py

    def quit_window(self):
        self.view.destroy()

    def display_some(self):
        self.view.display_label(self.model.dico_animaux[value])


if __name__ == "__main__":

    C = Controller()





# prochaine fois
# faire en sorte que l'on affiche toute la liste de tous les animaux
# du fichier a.txt, et que l'on puisse ajouter un animal, ou modifier un animal
# quand on supprimer on doit pouvoir supprimer sur la bonne ligne du fichier
# quand on add remise à zéro des champs








