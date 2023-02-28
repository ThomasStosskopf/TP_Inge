# TP 6 Ingénieurie Logiciel

by : Thomas Stosskopf

## Start the program

To start the program you can launch the controler.py script. 
It will call the vue.py script to open a window where you will see a list
of animal. You can display animal's attributs in the entries box bellow. 
You can then modify any animal.

## The vue.py script

Ths script communicate only with the controler.py script. 
vue.py is used to create a window where the user can add, modify or delete animals. 

## The controler.py script

The controler.py script communicate with the vue.py script
and the mode.py script. it is the link between these two. 

## Model.py

It is the script that will read and write in our 'database' a.txt. 
It is the only script to have access to a.txt. 
