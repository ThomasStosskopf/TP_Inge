# encoding : utf8
"""i dont know"""
from tkinter import *
from controler import *
class Application(Tk):
    def __init__(self, controller):
        """init view"""
        Tk.__init__(self)
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.creer_widgets()

    def creer_widgets(self):
        """init our widgets """
        self.label = Label(self, text="J'adore Python !")
        self.label1 = Label(self, text="")
        self.label_search = Label(self, text="Recherche")
        self.bouton_display = Button(self, text="Afficher", command=self.display_something)
        self.bouton = Button(self, text="Quitter", command=self.quit_window)
        self.bouton_add_animal = Button(self, text="Add", command=self.add_animal)

        self.search = Entry(self)
        self.entries = {}
        self.entries_label = {}

        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)

        self.label.pack()
        self.label1.pack()
        self.label_search.pack()
        self.search.pack()
        self.bouton_display.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.bouton.pack()
        self.bouton_add_animal.pack()

    def display_label(self, value):
        self.label1['text'] = value

    def display_something(self):
        self.controller.display(self.search.get())

    def quit_window(self):
        """method to quit the window"""
        self.controller.quit_window()

    def add_animal(self):
        dict_animal = {}
        for key in self.entries:
            dict_animal[key] = self.entries[key].get()
        self.controller.add_animal(dict_animal)

    def view_window(self):
        """method tp show our window"""
        self.title("Ma Première App")
        self.mainloop()


if __name__ == "__main__":
    app = Application(Controller)
    app.view_window()















