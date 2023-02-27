# encoding : utf8
"""model, used to write in the file a.txt """
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
        self.file = open(self.filename, "r+", encoding='utf-8')
        for line in self.file:
            line = line.strip()
            tab = line.split(",")
            a = Animal(tab[0], tab[1], tab[2], tab[3], tab[4])
            self.dico_animaux[a.name] = a


    def save(self, dict_animal):
        """
        method to save animal in the file a.txt
        """
        self.file = open(self.filename, "r+", encoding='utf-8')
        self.read_file()
        self.file.write( "\n" + dict_animal["species"] + ","+ dict_animal["age"]
                                + "," + dict_animal["diet"] + "," + dict_animal["foot"]
                                + "," + dict_animal["name"])
        self.close() # close file so it can be saved in the file without closing the app

    def modify_animal(self, dict_animal):
        print("Okay")
        # call the method to delete the right line
        self.delete_animal(dict_animal["name"])
        # reopen the file to write in it
        self.file=open(self.filename, "r+", encoding='utf-8')
        self.read_file()
        # write back the line with the new informations
        self.file.write("\n" + dict_animal["species"] + "," + dict_animal["age"]
                                + "," + dict_animal["diet"] + "," + dict_animal["foot"]
                                + "," + dict_animal["name"])
        self.close()  # close file so it can be saved in the file without closing the app


    def save_the_file(self):
        """save the file without empty line between lines"""
        with open(self.filename, "r+") as file_to_save:
            contents = file_to_save.read()
            contents = "\n".join(filter(lambda x: x.strip(), contents.split("\n")))
            file_to_save.seek(0)
            file_to_save.write(contents)
            file_to_save.truncate()


    def delete_animal(self, name_to_delete):
        """
        method to delete an animal from file and dictionary
        """
        #delete in dict
        for key in self.dico_animaux:
            if key == name_to_delete:
                del self.dico_animaux[key]
                break
        # open back the file
        self.file = open(self.filename, "r+", encoding='utf-8')

        # delete in file txt
        self.file.seek(0)  # Move the file cursor to the beginning of the file
        lines = self.file.readlines()  # Read all lines from the file
        self.file.seek(0)  # Move the file cursor back to the beginning of the file
        self.file.truncate()  # Clear the file contents
        for line in lines:
            line_list = line.strip().split(',')
            if line_list[-1] != name_to_delete:
                self.file.write(line)  # Write the line back to the file if the
                                        # animal name does not match the specified name
        self.close()  # close file so it can be saved in the file without closing the app


    def close(self):
        """
        method to close the file
        """
        self.save_the_file()
        self.file.close()

    def get_attributes(self) -> []:
        """method to get the attributes of the class Animal"""
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

    def get_name(self) -> []:
        """method to take the name of the animals"""
        list_name = []
        for keys in self.dico_animaux:
            list_name.append(keys)
        list_name.sort()
        return list_name

    def get_dict_attr(self, name):
        """
        method to get a dictionary of the chosen animal key will be the attributes
        and values will be the values of each attributes. We iterate with the build-in
         dir() method through all the attributes of the chosen object. Then we have
         to ignore the attributes which starts with '_', and we only get the attributes
         we have created.
        """
        dict_animal = {}
        animal = self.dico_animaux.get(name) # get the object 'animal' the user wants
        # Iterate through the attributes of the class Animal
        for attribute in dir(animal):
            # Ignore attributes that start with underscore (_) and are not defined in the class
            if not attribute.startswith("_"):
                # Get the value of the attribute
                value = getattr(animal, attribute)
                # Add the attribute and its value to the dictionary
                dict_animal[attribute] = value
        return dict_animal

if __name__ == "__main__" :
    model = Model("a.txt")
    model.read_file()
    print(model.get_dict_attr("Thomas"))
    model.close()
