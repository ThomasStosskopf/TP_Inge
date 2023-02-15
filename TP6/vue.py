# encoding : utf8
"""i dont know"""
from tkinter import *

class Application(Tk):
    def __init__(self, controller):
        """init view"""
        Tk.__init__(self)
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.namelist= self.controller.get_model_name()
        self.creer_widgets()

    def creer_widgets(self):
        """init our widgets """
        self.label = Label(self, text="J'adore Python !")
        self.label1 = Label(self, text="")
        self.label_search = Label(self, text="Recherche")
        self.bouton_display = Button(self, text="Afficher", command=self.display_something)
        self.bouton_leave = Button(self, text="Quitter", command=self.quit_window)
        self.bouton_add_animal = Button(self, text="Add", command=self.add_animal)
        self.button_delete = Button(self, text="Delete", command=self.del_animal)

        # Liste box here
        self.listboxname = Listbox(self)
        counter = 0
        for name in self.namelist:
            counter += 1
            self.listboxname.insert(counter, name)

        # entries box
        self.search = Entry(self)
        self.entries = {}
        self.entries_label = {}
        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)

        self.label.pack()
        self.label1.pack()
        self.label_search.pack()
        #self.search.pack() # we removed this on because we did thought it was usefull
        self.listboxname.pack()
        self.bouton_display.pack()
        # for loop to add entries box
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()

        # pack buttons :
        self.bouton_add_animal.pack()
        self.button_delete.pack()
        self.bouton_leave.pack()

    def display_label(self, value):
        self.label1['text'] = value

    def display_something(self):
        self.controller.display(self.listboxname.get(ACTIVE))

    def quit_window(self):
        """method to quit the window"""
        self.controller.quit_window()

    def add_animal(self):
        dict_animal = {}
        for key in self.entries:
            dict_animal[key] = self.entries[key].get()
            self.entries[key].delete(0, END)
        self.controller.add_animal(dict_animal)

    def del_animal(self):
        delete_name = self.listboxname.get(ACTIVE)
        self.controller.del_animal(delete_name)


    def view_window(self):
        """method tp show our window"""
        self.title("Ma Première App")
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.view_window()















