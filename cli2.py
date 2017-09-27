
from tkinter import *
from random import *
from socket import *
import threading
import time
b=[]
def lock():
    global b
    for j in b:
        j['state']='disable' 
def unlock():
    global b
    for j in b:
        j['state']='normal' 

def socksend(score):
    server.send(str.encode(str(score)))
    
def createbutton(i):
    
    global old
    global oldi
    global score
    print("old :",old)
    if old==1 :  
        old=l[i]
        oldi=i

    elif l[i]== old and oldi!=i:
        old=1
        oldi=i
        score=score+1
        b[i]['command'] = None
        b[oldi]['command'] = None
        player1_score["text"]=str(score)
        lock()
        server.send(str.encode("unlock"))
        socksend(score)
        
    elif l[i]!= old and oldi!=i: 
        print("startrefresh")
        target = lambda i = i : refreshthread(i)
        threading.Thread(target = target).start() 
        lock()
        server.send(str.encode("unlock"))

    b[i]['text']=l[i]   
    #if reply == "lock":
        #print("sssssss")
        #lock(b)               
HOST = 'localhost' 
#HOST = '10.0.1.32' 
PORT = 5000 
BUFFER_SIZE = 1024 
ADDRESS = (HOST, PORT) #(127.0.0.1, 5000) 
server = socket(AF_INET, SOCK_STREAM) #Create a socket  
server.connect(ADDRESS) #Connect it to a host 
l =  list(bytes.decode(server.recv(BUFFER_SIZE)) )

print(l)
root = Tk()
root.title("clientq1")
#root.geometry("200x280")

old=1
oldi=-1
score=0

start=server.send(str.encode("clintstart") )

f1 = Frame(root)
f1.pack( side=TOP)           
player1 = Label(f1, text = "Player1 :", width = 6, height = 2)
player1.grid(row = 0, column = 0)
player1_score = Label(f1, text = "0", width = 4, height = 2)
player1_score.grid(row = 0, column = 1)
player2 = Label(f1, text = "Player2 :", width = 6, height = 2)
player2.grid(row = 0, column = 2)
player2_score = Label(f1, text = "0", width = 4, height = 2)
player2_score.grid(row = 0, column = 3)  

def receivethread():
    while True:
        reply = bytes.decode(server.recv(BUFFER_SIZE))
        if reply == "unlock":
            unlock()

def refreshthread(i):
    time.sleep(0.5)
    global oldi
    global old
    b[i]['text']=""
    b[oldi]['text']=""
    old = 1 
    oldi = i       

for i in range(4):
    fkey = Frame(root)
    fkey.pack( side=LEFT,expand=YES, fill=BOTH)     
    for j in range(5):
        b.append(Button(fkey, text="",bg="lightblue",font = "Helvetica 16 bold italic",fg="black",bd=5 ,command=lambda x=i,y=j : createbutton(y+x*5),width=2))
        b[j+i*5].pack()    

while True: 
    reply = bytes.decode(server.recv(BUFFER_SIZE))
    if str(reply):
        lock()
    if not reply: 
        print('Server disconnected') 
        break
    print("end")
    threading.Thread(target = receivethread).start()
    root.mainloop()
    #while True:
        #print("asddd")
        #reply = bytes.decode(server.recv(BUFFER_SIZE))
        #if str(reply):
                #print(reply)
      
