from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("200x280")
#----------------------------------------Menu------------------------------------------------------------------------------------
menubar=Menu(root)
root.config(menu=menubar)

def a():
    x.set(x.get() + char)
    print(char)
#------------------------------------------------Cal--------------------------------------------------------------------------------------------------------------
b=[]
ff=16
f1=Frame(root,bg="blue").pack()
x=StringVar()    
entry=Entry(f1,bg="lightblue",justify=RIGHT,fg="blue",bd=10, font = "Helvetica 16 bold italic",textvariable=x)
entry.pack(fill=X)
for key in ("741C", "8520", "963.", "/*+-="):
    fkey = Frame(root)
    fkey.pack( side=LEFT,expand=YES, fill=BOTH)            
    for char in key:
        if char == '=':
            btn =Button(fkey, text=char,bg="lightsteelblue",font = "Helvetica 16 bold italic",fg="black",bd=5) 
            btn.pack(side=TOP, expand=YES, fill=BOTH)
            btn.bind('<ButtonRelease-1>',lambda null: x.set(eval(x.get())))
            #b.bind("<Enter>",lambda e:btn.configure(font = "Helvetica 22 bold italic"))
            #b.bind("<Leave>",lambda e:btn.configure(font = "Helvetica 16 bold italic"))
        elif char == 'C':         
            Button(fkey, text=char,bg="lightblue",font = "Helvetica 16 bold italic",fg="red",bd=5,command=lambda num=x, c=char: num.set("")).pack(side=TOP,fill=BOTH, expand=YES)
            
        else:
            b = Button(fkey, text=char,bg="azure",font = "Helvetica %d bold italic"%ff,fg="black",bd=5,command=lambda num=x, c=char:num.set(num.get() + c) )
            #b.append(Button(fkey, text=char,bg="azure",font = "Helvetica %d bold italic"%ff,fg="black",bd=5,command=lambda num=x, c=char:num.set(num.get() + c) ))
            #b[j+i*5].pack()
            #b.bind("<Enter>",lambda e:b.configure(font = "Helvetica 22 bold italic"))
            #b.bind("<Enter>",lambda e:b.configure(font = "Helvetica 22 bold italic"))
            #b.bind("<Leave>",lambda e:b.configure(font = "Helvetica 16 bold italic"))            
            b.pack( expand=YES, fill=BOTH)

root.mainloop()