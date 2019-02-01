__author__ = "Гонцов Александр Евгеньевич"

Task 1, easy, file_name - creator.py

import os

def creator(dirname):
    try:
        os.mkdir(dirname)
    except Exception:
        print("Can't create directory ", dirname)

def C_multiply():
    for index in range(1, 10):
        creator("dir_", str(1))

C_multiply ()

Task 2, easy, file_name - remover.py

import os

def remover(dirname):
    try:
        os.rmdir(dirname)
    except Exception:
        print("Can't remove directory ", dirname)

def R_multiply():
    for index in range(1, 10):
        remover("dir_", str(1))

R_multiply ()

Task 3, easy, file_name - copymaker.py

import os

def copymaker(s, d):
	open(s, "r", encoding-"UTF-8"), open(d, "w", encoding-"UTF-8"): d.write(s.read())

copymaker(os.path.basename(__file__), os.path.basename(__file__), "_copy.py")

Task 4, easy, file_name - disclosure.py

import os

def disclosure():
	for index in os.listdir():
		if os.path.isdir(index):
		print(index)

disclosure()

Task 1, normal, file_name - resume.py

import creator
import remover
import copymaker
import disclosure

answer = "" # чтобы не было ошибки, и мы зашли в цикл
while answer != "q": # начало цикла
answer = input("Do you want to work? y or n or q")
if answer == "y":
	print("Great!")
	print("What would you like me to do?")
	print("[1] <dirname> - create new directories")
	print("[2] - remove directories")
	print("[3] - make a copy")
	print("[4] - show all the files in the current directory")
	do = int(input("The action number:"))
	if do == 1:
		C_multiply
		print ("Success")
	elif do == 2:
		R_multiply
		print ("Success")
	elif do == 3: 
		copymaker(os.path.basename(__file__), os.path.basename(__file__), "_copy.py")
		print ("Success")
	elif do == 4:
		disclosure()	
	else:
		pass
elif answer == "n":
	print("Goodbye, have a nice day!")
else:
	print("Undefined answer, I need to look for it in a dictionary")