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


    def control_give_dict(self, dico):
        return self.model.get_dict_attr(dico)

# utiliser le dictionnaire animal attribut avec sa valeur

    def add_animal(self, dict_animal):
        """Method to save an animal in our dict"""
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
