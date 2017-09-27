from tkinter import *
from random import *
from socket import *
import threading

BUFFER_SIZE = 1024 
ADDRESS = ('localhost', 5001) 
server = socket(AF_INET, SOCK_STREAM) 
server.connect(ADDRESS) 
l =  list(bytes.decode(server.recv(BUFFER_SIZE)) );print(l)#***************************1
# l=list("AABBCCDDEEFFGGHHIIJJ");print(l)
#--------------------------------------------------------------------------
root = Tk()
root.title("client")
root.geometry("200x310")
root.configure(background='wheat')
b=[]
passed=[]
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
        if score[0]<score[1]:
            status['text']="You WIN"
        elif score[0]>score[1]:
            status['text']="You LOSS"
            status['width']=8
        else:
            status['text']="DRAW"
def clickButton(i):
    b[i]['text']=l[i]
    b[i]['bg']='dodgerblue'
    global oldi
    global first
    server.send(str.encode(str(i)))
    if first:
        print("first")
        first=False
        oldi=i
    elif l[i]== l[oldi] and oldi!=i:
        print("i : %d oldi: %d ---same"%(i,oldi))
        b[oldi]['state']='disable'
        b[i]['state']='disable'
        score[1]=score[1]+10
        player2_score["text"]=str(score[1])
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
        b[oldi]['bg']='lightblue'
        b[i]['bg']='lightblue'
        oldi=i
        lock()
        # server.send(str.encode("unlock"+''.join(passed)))
        server.send(str.encode("cunlock"))
first2=True   
def sendClick(i):
    print("test---",l[i])
    b[i]['text']=l[i]
    b[i]['bg']='hotpink'
    global oldi
    global first2
    global score
    # server.send(str.encode(str(i)))
    if first2:
        print("first")
        first2=False
        oldi=i
    elif l[i]== l[oldi] and oldi!=i:
        print("+++++i : %d oldi: %d ---same"%(i,oldi))
        b[oldi]['state']='disable'
        b[i]['state']='disable'
        score[0]=score[0]+10
        player1_score["text"]=str(score[0])
        # d=False
        first2=True
        end()
        # passed.append(oldi)
        # passed.append(i)
        # print(passed)
    elif l[i]!= l[oldi]  :
        print("+++++i : %d oldi: %d ---dont"%(i,oldi))
        b[i]['text']=""
        b[oldi]['text']=""
        oldi=i

        # server.send(str.encode("unlock"+''.join(passed)))
 
def lock():
    global b
    for j in b:
        j['state']='disable' 
        j['bg']='snow3'
    print("Locking")
def unlock():
    global b
    global first
    for j in b:
        if j['text'] == "":
            j['state']='normal' 
            j['bg']='lightblue'  
        # else:
        #     j['bg']='hotpink'          
    first=True
    print("Unlocking")   
def receivethread():
    while True:
        reply = bytes.decode(server.recv(BUFFER_SIZE))
        print("reply : ",reply)
        if reply == "sunlock":
            print("reply sunlock")
            unlock()
        if reply == "serverstart":
            print("reply serverstart")           
        if reply in [str(x) for x in range(20)]:
            print("in",reply)
            sendClick(int(reply))
            # b[int(reply)]['text']=l[int(reply)] 
        if reply[0] == "zu":
            print("uuuuuuuuuunlock")
            passed=passed+list(bytes.decode(server.recv(BUFFER_SIZE)) )
            print(passsed)
            unlock()

server.send(str.encode("clintstart") )
f2 = Frame(root,bg="lightblue")
f2.pack( side=TOP,expand=YES, fill=BOTH)           
player2 = Label(f2, text = ": Player2",font = "Helvetica 12 bold italic",fg="deeppink", justify=RIGHT,bg='lightblue')
player2.pack(side=RIGHT)
player2_score = Label(f2, text = "0",font = "Helvetica 18 bold italic",fg="deeppink",bg='lightblue')
player2_score.pack(side=RIGHT)
f1=Frame(root)
f1.pack( side=TOP)
for button_row in range(5):
    fkey = Frame(f1)
    fkey.pack( side=TOP,expand=YES, fill=BOTH)     
    for button_col in range(4):
        b.append(Button(fkey, text="",bg="lightblue",font = "Helvetica 16 bold italic",fg="black",bd=5 ,command=lambda x=button_row,y=button_col : clickButton(y+x*4),width=2))
        b[button_col+button_row*4].pack(side=LEFT)
f3 = Frame(root,bg='lightpink')
f3.pack( side=TOP,expand=YES, fill=BOTH) 
player1 = Label(f3, text = "Player1 :",font = "Helvetica 12 bold italic",fg="deeppink", justify=LEFT,bg='lightpink')
player1.pack(side=LEFT)
player1_score = Label(f3, text = "0",font = "Helvetica 18 bold italic",fg="deeppink",bg='lightpink')
player1_score.pack(side=LEFT)
while True: 
    reply = bytes.decode(server.recv(BUFFER_SIZE))
    print("server : ",reply)
    if str(reply):
         lock()
    if not reply: 
        print('Server disconnected') 
        break
    print("end")
    threading.Thread(target = receivethread).start()
    root.mainloop()