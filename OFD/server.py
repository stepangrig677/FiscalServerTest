
import socket
import datetime

sock = socket.socket()
sock.bind(('', 12000))
sock.listen(1)

def Time():
    return str(datetime.datetime.now().minute) +"_"+ str(datetime.datetime.now().second)+"_"+ str(datetime.datetime.now().microsecond)

def CreateResponse():
    Html = "<html><body><h1>It works!</h1></body></html>"
    Str = "HTTP/1.1 200 OK\nContent-type: text/html\nContent-Length:" + str(len(Html)) + "\n\n" + Html
    return Str#bytes(Str)


def Accept():
    conn, addr = sock.accept()

    print ('connected:')
    global N
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(CreateResponse())

        f = open("saved/"+ Time()+"srv", "wb")
        f.write(data)
    conn.close()


while True:
    Accept()
