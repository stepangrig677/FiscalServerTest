import socket
import datetime


def Time():
    return str(datetime.datetime.now().minute) +"_"+ str(datetime.datetime.now().second)+"_"+ str(datetime.datetime.now().microsecond)


host='kkm-server-test.1-ofd.ru'
port = 7777

#host='localhost'
#port =  12000


f = open('Start', 'rb')
Message = f.read()

sock = socket.socket()
sock.connect((host, port))

sock.send(Message)
data = sock.recv(1024)
print('ok')
f = open("saved/"+Time()+"cli", "wb")
f.write(data)

sock.close()