import threading
import time
from tkinter import *
from random import *
from socket import * 
HOST = 'localhost'
PORT = 5000 
BUFFER_SIZE = 1024 
ADDRESS = (HOST, PORT) #('127.0.0.1', 5000) 
def clickButton(i):
    global oldi
    print("i : %d oldi: %d"%(i,oldi))
    if l[i]== l[oldi] and oldi!=i:
        b[oldi]['state']='disable'
        b[i]['state']='disable'
        oldi=-1
        print("same",oldi)
    elif l[i]!= l[oldi] :
        b[oldi]['text']=""
        oldi=i
        print("dont")
        lock()
        client.send(str.encode("unlock")) 
    b[i]['text']=l[i]
def lock():
    global b
    for j in b:
        j['state']='disable' 
def unlock():
    global b
    for j in b:
        j['state']='normal' 
def receivethread():
    while True:
        reply = bytes.decode(client.recv(BUFFER_SIZE))
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
server = socket() 
server.bind(ADDRESS)
server.listen(1) 
l=[]

def createbutton(i):
        b[i]['text']=l[i]
        client.send(str.encode(str(i)))
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
            socksend(score)
            lock()
            client.send(str.encode("unlock"))

        elif l[i]!= old and oldi!=i: 
            print("startrefresh")
            target = lambda i = i : refreshthread(i)
            threading.Thread(target = target).start()
            lock()
            client.send(str.encode("unlock"))  
        #client.send(str.encode(str(i)))
def socksend(score):
    
    client.send(str.encode(str(score)))
    
https://bitbucket.org/fotosyn/fotosynlabs/raw/9819edca892700e459b828517bba82b0984c82e4/BerryCam/berryCam.py

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
    client.send(str.encode("serverstart") )
    
    
    root = Tk()
    root.title("q1")

    #root.geometry("200x280")



    ##l=sample(range(65, 65 + 25),10)
    #new()
    old=1
    oldi=-1
    score=0
   
 
    b=[]
    for i in range(4):
        fkey = Frame(root)
        fkey.pack( side=LEFT,expand=YES, fill=BOTH)     
        for j in range(5):
            b.append(Button(fkey, text="",bg="azure",font = "Helvetica 16 bold italic",fg="black",bd=5 ,command=lambda x=i,y=j : createbutton(y+x*5),width=2))
            b[j+i*5].pack()    
    while True:         
        message = bytes.decode(client.recv(BUFFER_SIZE)) 
        if not message: 
            print("Client diconnected") 
            client.close()
            break 
        else: 
            print(message) 
            client.send(str.encode(str(score))) 
        #message = bytes.decode(client.recv(BUFFER_SIZE)) 
        threading.Thread(target = receivethread).start()       
        root.mainloop()
                               