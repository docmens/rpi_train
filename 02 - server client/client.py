
import time
import socket

#use header to announce how long the message will be
HEADERSIZE = 10

#establish connection with server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
#s.connect(('192.168.126.9',1234))

while True:

    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")
        print(msg.decode("utf-8"))
        print(len(msg))

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''

print(msg_full)

time.sleep(1)
s.send(bytes("message to the server","utf-8"))


#for i in range(10):
#    print('client: ' + str(i))
#    time.sleep(2)
