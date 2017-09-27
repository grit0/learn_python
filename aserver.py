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
value=list("AABBCCDDEEFFGGHHIIJJ")
# l=list(" "*20)
l=value
passed=[]
b=[]
old=1
oldi=-1
first=True
score=[0,0]
def end():
    global score
    if score[0]+score[1]==100 :
        print("END")
        f1.destroy()
        status = Label(root, text = "You WIN",font = "Helvetica 28 bold italic",fg="maroon",bd=10, width = 6, height = 2)
        status.pack()
        if score[0]>score[1]:
            status['text']="You WIN"
        elif score[0]<score[1]:
            status['text']="You LOSS"
            status['width']=8
        else:
            status['text']="DRAW"
def lock():
    print("Locking")
    global b
    for j in b:
        j['state']='disable' 
        j['bg']='snow3'
def unlock():
    global b
    global first
    for j in b:
        if j['text'] == "":
            j['state']='normal' 
            j['bg']='pink'
        # else:
        #     j['bg']='hotpink'

    first=True
    print("Unlocking")  
def receivethread():
    while True:
        global first
        reply = bytes.decode(client.recv(BUFFER_SIZE))
        print("reply : ",reply)
        if reply == "cunlock":
            print("reply unlock")
            unlock()
        if reply == "serverstart":
            print("reply serverstart")           
        if reply in [str(x) for x in range(20)]:
             print("in",reply)

             sendClick(int(reply))
        if score[0]+score[1]==100 :
            print("END")
            f1.destroy()
            if score[0]>score[1]:
                player1 = Label(root, text = "win :", width = 6, height = 2)
                player1.pack()

        # b[int(reply)]['text']=l[int(reply)] 
# def refreshthread(i):
#     time.sleep(0.5)
#     global oldi
#     global old
#     b[i]['text']=""
#     b[oldi]['text']=""
#     old = 1 
#     oldi = i
def clickButton(i):
    b[i]['text']=l[i]
    b[i]['bg']='hotpink'
    global oldi
    global first
    global score
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
        # d=False
        first=True
        end()


        # passed.append(oldi)
        # passed.append(i)
        # print(passed)

    elif l[i]!= l[oldi]  :
        print("i : %d oldi: %d ---dont"%(i,oldi))
        b[i]['text']=""
        b[oldi]['text']=""
        b[oldi]['bg']='pink'
        b[i]['bg']='pink'
        oldi=i
        lock()
        client.send(str.encode("sunlock"))
        # client.send(str.encode("unlock"+''.join(passed))) 
        # client.send(str.encode(''.join(passed)) )

        #client.send(str.encode(str(i)))
# def socksend(score):
#     client.send(str.encode(str(score)))
first2=True
def sendClick(i):
    b[i]['text']=l[i]
    b[i]['bg']='dodgerblue'
    global oldi
    global first2
    global score
    # server.send(str.encode(str(i)))
    if first2:
        print("first")
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
        # d=False
        first2=True
        end()
        # passed.append(oldi)
        # passed.append(i)
        # print(passed)
    elif l[i]!= l[oldi]  :
        print("++++i : %d oldi: %d ---dont"%(i,oldi))
        b[i]['text']=""
        b[oldi]['text']=""
        # b[oldi]['bg']='pink'
        # b[i]['bg']='pink'
        oldi=i

while True: 
    print('waiting for connection...')
    client, address = server.accept()             
    print('connected from: ', address)
    client.send(str.encode(''.join(l)) )  
    client.send(str.encode("serverstart") )
    
    root = Tk()
    root.title("server")
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
            # client.send(str.encode(str(score))) 
        #message = bytes.decode(client.recv(BUFFER_SIZE)) 
        threading.Thread(target = receivethread).start() 


        root.mainloop()
    

