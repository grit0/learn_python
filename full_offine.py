from tkinter import *
from random import *
root = Tk()
root.title("q1")
l=list("AABBCCDDEEFFGGHHIIJJ");print(l)
first=True
d=True
oldi=-1
def clickButton(i):
    global oldi
    global first
    global d
    if first:
        print("first")
        first=False
        oldi=i
    elif l[i]== l[oldi] and oldi!=i:
        print("i : %d oldi: %d ---same"%(i,oldi))
        b[oldi]['state']='disable'
        b[i]['state']='disable'
        # d=False
        first=True
    elif l[i]!= l[oldi]  :
        print("i : %d oldi: %d ---dont"%(i,oldi))
        b[oldi]['text']=""
        oldi=i

    b[i]['text']=l[i]
    
b=[]
for button_row in range(5):
    fkey = Frame(root)
    fkey.pack( side=TOP,expand=YES, fill=BOTH)     
    for button_col in range(4):
        b.append(Button(fkey, text="",bg="azure",font = "Helvetica 16 bold italic",fg="black",bd=5 ,command=lambda x=button_row,y=button_col : clickButton(y+x*4),width=2))
        b[button_col+button_row*4].pack(side=LEFT)

# b[5]['text']="ddd"
# b[2].bind("<Enter>", lambda e:b[1].config(font = "Helvetica 22 bold italic"))

root.mainloop()