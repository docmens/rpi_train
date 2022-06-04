
import time

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
#s.connect(('192.168.126.9',1234))

msg_full = ''
while True:
    msg = s.recv(8)
    msg_full += msg.decode("utf-8")
    print(msg.decode("utf-8"))
    print(len(msg))
    if len(msg) < 8:
        break

print(msg_full)

time.sleep(1)
s.send(bytes("message to the server","utf-8"))


#for i in range(10):
#    print('client: ' + str(i))
#    time.sleep(2)
