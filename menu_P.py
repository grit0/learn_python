
import threading
import time
from tkinter import *
from random import *
from socket import *
root = Tk()
root.title("q1")
#root.geometry("200x280")




l=[]
def list_Samplee():
    global l
    l=[chr(i) for i in range(65, 65 + 10)]*2
    print(l)
def list_Random():
    global l
    l=[chr(i) for i in sample(range(65, 65 + 25), 10)]*2
    shuffle(l)
    print(l)

menubar=Menu(root)
root.config(menu=menubar)
file_menu=Menu(menubar)
edit_menu=Menu(menubar)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_checkbutton(label="Random",command=list_Random)
file_menu.add_checkbutton(label="Sample",command=list_Samplee)
file_menu.add_separator()
file_menu.add_command(label="Quit",command=root.quit)


print(l)


root.mainloop()