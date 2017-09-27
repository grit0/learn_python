import socket
server = socket.socket()         
HOSTNAME = socket.gethostbyname(socket.gethostname())
PORT = 55555               
server.bind((HOSTNAME,PORT))      
server.listen(5)
print("Wait connect.....")
client,addr = server.accept()    
print('Connection from', addr)   
data="Thank you"
while True:
	client.send(data.encode('utf-8'))
client.close()                