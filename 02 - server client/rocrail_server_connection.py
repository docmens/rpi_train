#!/usr/bin/python
# Rocrail XML script example: Power ON.
 
#from socket import AF_INET,SOCK_STREAM,socket
import socket as sk

# Subroutine for adding the XML-Header and send it to the server
def sendMsg( s, xmlType, xmlMsg ):
  message = "<xmlh><xml size=\"%d\" name=\"%s\"/></xmlh>%s" %(len(xmlMsg), xmlType, xmlMsg)
  print message
  s.send(message)
 
# Create the server connection
s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
s.connect(('localhost', 8051))
 
# Compose the power on command and send it
rrMsg = "<sys cmd=\"go\"/>"
sendMsg( s, "sys", rrMsg )
 
# Close server connection
s.close()