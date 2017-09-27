import threading
import time
from tkinter import *
from random import *
from socket import * 
BUFFER_SIZE = 1024 
ADDRESS = ('localhost', 5001)
server = socket() 
server.bind(ADDRESS)
server.listen(10) 
# l=list("AABBCCDDEEFFGGHHIIJJ")
l=[chr(i) for i in sample(range(65, 65 + 25), 10)]*2
shuffle(l)
for x in range(0,20,4):
	print(l[x:x+4])

enemy=[]
b=[]
old=1
oldi=-1
first=True
score=[0,0]
def end():
    global score
    if score[0]+score[1]==100 :
        f1.destroy()
        status = Label(root, text = "You WIN",font = "Helvetica 28 bold italic",fg="maroon",bd=10, width = 6, height = 2)
        status.pack()
        if score[0]>score[1]:
            status['text']="You WIN"
        elif score[0]<score[1]:
            status['text']="You LOSE"
            status['width']=8
        else:
            status['text']="DRAW"
        print("END")
def lock():
    print("Locking")
    global b
    global enemy
    print("enemy : ",enemy)
    for i in range(20):
        b[i]['state']='disable' 
        b[i]['bg']='snow3'
        if b[i]['text'] == "":
            b[i]['bg']='snow3'
        elif i in enemy:
            b[i]['bg']='dodgerblue'
        else:
            b[i]['bg']='hotpink'
def unlock():
    time.sleep(1)
    global b
    global first
    for j in b:
        if j['text'] == "":
            j['state']='normal' 
            j['bg']='pink'
    first=True
    print("Unlocking")  
def receivethread():
    while True:
        global first
        reply = bytes.decode(client.recv(BUFFER_SIZE))
        print("reply : ",reply)
        if reply == "cunlock":
            # print("reply unlock")
            unlock()
        if reply == "serverstart":
            print("reply serverstart")           
        if reply in [str(x) for x in range(20)]:
             sendClick(int(reply))

def refreshthread(i):
    time.sleep(0.5)
    global oldi
    b[i]['text']=""
    b[oldi]['text']=""
    b[oldi]['bg']='snow3'
    b[i]['bg']='snow3'
    oldi=i

def clickButton(i):
    b[i]['text']=l[i]
    b[i]['bg']='hotpink'
    global oldi
    global first
    client.send(str.encode(str(i)))
    if first:
        print("i : %d oldi: %d ---first"%(i,oldi))
        first=False
        oldi=i
    elif l[i]== l[oldi] and oldi!=i:
        print("i : %d oldi: %d ---same"%(i,oldi))
        b[oldi]['state']='disable'
        b[i]['state']='disable'
        score[0]=score[0]+10
        player1_score["text"]=str(score[0])
        first=True
        end()

    elif l[i]!= l[oldi]  :
        print("i : %d oldi: %d ---dont"%(i,oldi))
        target = lambda i = i : refreshthread(i)
        threading.Thread(target = target).start()
        lock()
        client.send(str.encode("sunlock"))
first2=True
def sendClick(i):
    b[i]['text']=l[i]
    b[i]['bg']='dodgerblue'
    global oldi
    global first2
    global score
    global enemy
    if first2:
        print("++++++i : %d oldi: %d ---first"%(i,oldi))
        first2=False
        oldi=i
    elif l[i]== l[oldi] and oldi!=i:
        print("++++i : %d oldi: %d ---same"%(i,oldi))
        b[oldi]['state']='disable'
        b[i]['state']='disable'
        score[1]=score[1]+10
        player2_score["text"]=str(score[1])
        # b[oldi]['state']='hotpink'
        # b[i]['bg']='hotpink'
        first2=True
        enemy.append(i)
        enemy.append(oldi)
        end()

    elif l[i]!= l[oldi]  :
        print("++++i : %d oldi: %d ---dont"%(i,oldi))
        target = lambda i = i : refreshthread(i)
        threading.Thread(target = target).start()
        first2=True

while True: 
    print('waiting for connection...')
    client, address = server.accept()             
    print('connected from: ', address)
    client.send(str.encode(''.join(l)) )  
    client.send(str.encode("serverstart") )
    
    root = Tk()
    root.title("P1 server")
    root.geometry("200x310")
    root.configure(background='wheat')
    f3 = Frame(root,bg='lightpink')
    f3.pack( side=TOP,expand=YES, fill=BOTH) 
    player1 = Label(f3, text = "Player1 :",font = "Helvetica 12 bold italic",fg="deeppink", justify=LEFT,bg='lightpink')
    player1.pack(side=LEFT)
    player1_score = Label(f3, text = "0",font = "Helvetica 18 bold italic",fg="deeppink",bg='lightpink')
    player1_score.pack(side=LEFT)

    f1=Frame(root)
    f1.pack( side=TOP)
    for button_row in range(5):
        fkey = Frame(f1)
        fkey.pack( side=TOP,expand=YES, fill=BOTH)     
        for button_col in range(4):
            b.append(Button(fkey, text="",bg="pink",font = "Helvetica 16 bold italic",fg="maroon",bd=5 ,command=lambda x=button_row,y=button_col : clickButton(y+x*4),width=2))
            b[button_col+button_row*4].pack(side=LEFT) 
    f2 = Frame(root,bg="lightblue")
    f2.pack( side=TOP,expand=YES, fill=BOTH)           
    player2 = Label(f2, text = ": Player2",font = "Helvetica 12 bold italic",fg="deeppink", justify=RIGHT,bg='lightblue')
    player2.pack(side=RIGHT)
    player2_score = Label(f2, text = "0",font = "Helvetica 18 bold italic",fg="deeppink",bg='lightblue')
    player2_score.pack(side=RIGHT)

              
    while True:         
        message = bytes.decode(client.recv(BUFFER_SIZE)) 
        if not message: 
            print("Client diconnected") 
            client.close()
            break 
        else: 
            print("client : ",message) 
        threading.Thread(target = receivethread).start() 
        root.mainloop()
 