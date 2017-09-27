from tkinter import *
from random import *
from socket import * 
HOST = 'localhost'
PORT = 5000 
BUFFER_SIZE = 1024 
ADDRESS = (HOST, PORT) #('127.0.0.1', 5000) 
def lock(a):
    for j in range(20):
        a[j]['state']='disable' 
def unlock(a,i):
    for j in i:
        print(j)
        a[j]['state']='disable' 
server = socket() 
server.bind(ADDRESS)
server.listen(1) 

l=[]
passed=[]
def socksend(score,passed):
    print("socksend")
    client.send(str.encode(str(score)))
def new():
    global l
    del l[:]
    for i in sample(range(65, 65 + 25), 10):
        l.append(chr(i))
    l=l+l
    shuffle(l)
    print(l)

def samplee():
    global l
    del l[:]
    for i in range(65, 65 + 10):
        l.append(chr(i))
    l=l+l
    print(l)    
samplee()
while True: 
    print('waiting for connection...')
    client, address = server.accept()             
    print('connected from: ', address)
    client.send(str.encode(''.join(l)) )  
    client.send(str.encode("start") )
           
    while True: 
     
        root = Tk()
        root.title("q1")
        
        #root.geometry("200x280")
        
        menubar=Menu(root)
        root.config(menu=menubar)
        file_menu=Menu(menubar)
        edit_menu=Menu(menubar)
        
        menubar.add_cascade(label="File",menu=file_menu)
        
        file_menu.add_checkbutton(label="Random",command=new)
        file_menu.add_checkbutton(label="Sample",command=samplee)
        
        file_menu.add_separator()
        file_menu.add_command(label="Quit",command=root.quit)
        
        
        ##l=sample(range(65, 65 + 25),10)

        #new()
        old=1
        oldi=-1
        score=0

        def a(i):
        
                global old
                global oldi
                global score
                print("old :",old)
                if old==1 :  
                    old=l[i]
                    oldi=i
            
                elif l[i]== old and oldi!=i:
                    old=1
                    #b[oldi]['state']='disable'
                    passed.append(oldi)
                    oldi=i
                    #b[i]['state']='disable'
                    passed.append(i)
                    score=score+1
                    print(passed)
                    unlock(b,passed)
                    player1_score["text"]=str(score)
                    socksend(score,passed)
                    

                    lock(b)
                            
                             
                else:      
                    b[oldi]['text']=""    
                    old=l[i]
                    oldi=i
                b[i]['text']=l[i]       
        f1 = Frame(root,bg="red")
        f1.pack()     


        player1 = Label(f1, text = "Player1 :", width = 6, height = 2)
        player1.grid(row = 0, column = 0)
        player1_score = Label(f1, text = "0", width = 4, height = 2)
        player1_score.grid(row = 0, column = 1)
        player2 = Label(f1, text = "Player2 :", width = 6, height = 2)
        player2.grid(row = 0, column = 2)
        player2_score = Label(f1, text = "0", width = 4, height = 2)
        player2_score.grid(row = 0, column = 3)  
        b=[]
        for i in range(4):
            fkey = Frame(root)
            fkey.pack( side=LEFT,expand=YES, fill=BOTH)     
            for j in range(5):
                b.append(Button(fkey, text="",bg="azure",font = "Helvetica 16 bold italic",fg="black",bd=5 ,command=lambda x=i,y=j : a(y+x*5),width=2))
                #b=Button(fkey, text="",bg="azure",font = "Helvetica 16 bold italic",fg="black",bd=5 ,command=lambda x=i,y=j : a(y+x*5),width=2)
                #b.pack()
        
                b[j+i*5].pack()
        
        message = bytes.decode(client.recv(BUFFER_SIZE)) 
        
        if not message: 
            print("Client diconnected") 
            client.close()
            break 
        else: 
            print(message) 
            client.send(str.encode(str(score))) 
        #message = bytes.decode(client.recv(BUFFER_SIZE)) 
     
        root.mainloop()
    

