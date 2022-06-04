
import time
import socket

#use header to announce how long the message will be
HEADERSIZE = 10

#establish connection with client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())
s.bind((socket.gethostname(),1234))
s.listen(5)



while True:
    print('test')
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg #left align

    clientsocket.send(bytes(msg, "utf-8"))
    time.sleep(1)

    #msg = clientsocket.recv(1024)
    #print(msg.decode("utf-8"))


#for i in range(10):
#    print('server: ' + str(i))
#    time.sleep(2)
