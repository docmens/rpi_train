
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    print('test')
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
    time.sleep(1)

    #msg = clientsocket.recv(1024)
    #print(msg.decode("utf-8"))




#for i in range(10):
#    print('server: ' + str(i))
#    time.sleep(2)
