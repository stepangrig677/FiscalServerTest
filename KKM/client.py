import socket
import datetime


def Time():
    return str(datetime.datetime.now().minute) +"_"+ str(datetime.datetime.now().second)+"_"+ str(datetime.datetime.now().microsecond)

print(Time())

f = open('Start', 'rb')
Message = f.read()

sock = socket.socket()
sock.connect(('localhost', 12000))

# while(True):

sock.send(Message)
data = sock.recv(1024)
print(data)
f = open("saved/"+Time()+"cli", "wb")
f.write(data)

sock.close()