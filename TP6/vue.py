# encoding : utf8
"""i dont know"""
from tkinter import *

class Application(Tk):
    def __init__(self, controller):
        """init view"""
        Tk.__init__(self)
        self.creer_widgets()
        self.controller = controller

    def quit_window(self):
        """method to quit the window"""
        self.controller.quit_window()




    def creer_widgets(self):
        """init our widgets """
        self.label1 = Label(self, text= "")
        self.label = Label(self, text="J'adore Python !")
        self.bouton_display = Button(self, text="display something", command=self.display_something)
        self.bouton = Button(self, text="Quitter", command=self.quit_window)
        self.search = Entry(self)
        self.attributes = ["species", "age", "diet", "foot", "name"]


        self.species = Entry(self)
        self.age = Entry(self)
        self.diet = Entry(self)
        self.foot = Entry(self)
        self.name = Entry(self)
        self.search.pack()
        self.label.pack()
        self.label1.pack()
        self.bouton_display.pack()
        self.bouton.pack()

    def display_label(self, value):
        self.label1["text"] = value

    def display_something(self):
        self.controller.display_some()

    def view_window(self):
        """method tp show our window"""
        self.title("Ma Première App")
        self.mainloop()





if __name__ == "__main__":
    pass
















