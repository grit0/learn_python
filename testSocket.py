import socket
 
TCP_IP = "192.168.1.151"
TCP_PORT = 8081
BUFFER_SIZE = 1024
MESSAGE = socket.gethostbyname(socket.gethostname())
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT)) 
s.send(MESSAGE.encode('utf-8')) 
data = s.recv(BUFFER_SIZE) 
s.close() 
 
print("received data:", data) 