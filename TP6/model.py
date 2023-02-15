# encoding : utf8
"""model """
from animal import Animal


class Model():
    def __init__(self, filename):
        self.filename = filename
        self.file=open(self.filename, "r")
        self.dico_animaux = {}

    def read_file(self):
        for line in self.file:
            line = line.strip()
            tab = line.split(",")
            a = Animal(tab[0],tab[1],tab[2],tab[3],tab[4])
            self.dico_animaux[a.name] = a

    def close(self):
        self.file.close()

if __name__ == "__main__" :
    model = Model("a.txt")
    model.read_file()
    print(model.dico_animaux["Rochelle"])




