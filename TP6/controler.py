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
        self.view.display_label(self.model.get_dict_attr(value))


# utiliser le dictionnaire animal attribut avec sa valeur

    def add_animal(self, dict_animal):
        """
        Method to save/modify an animal in our dict
        The controller chose the right model.py function to write into the file
        """
        # list of animal's names that are already in the file
        list_actual_animals = self.model.get_name()

        # verify if the name in the entry box is already in the list or not
        # if it is, then we call the function from model to modify the line in the file
        if dict_animal["name"] in list_actual_animals:
            print("Animal ", dict_animal["name"], " Modified!")
            self.model.modify_animal(dict_animal)

        # if it is not, then it is a new animal, and we can just add it at the end of the file
        if dict_animal["name"] not in list_actual_animals:
            print("add animal")
            self.model.save(dict_animal)


    def get_model_entries(self):
        """get the list of the attributes with the method in model"""
        return self.model.get_attributes()

    def quit_window(self):
        """
        method to quit the window
        """
        print("close app")
        self.model.close()
        self.view.destroy()

    def get_model_name(self):
        """method to get the list of name from model.py
         so we can give it to the view.
         """
        return self.model.get_name()

    def del_animal(self, name_to_delete):
        """
        take the name to delete from the view
        so we can give it to the model
        """
        self.model.delete_animal(name_to_delete)


if __name__ == "__main__":
    C = Controller()
