
import socket
import datetime

sock = socket.socket()
sock.bind(('', 10000))
sock.listen(1)

def Time():
    return str(datetime.datetime.now().day) +"_"+str(datetime.datetime.now().hour) +"_"+str(datetime.datetime.now().minute) +"_"+ str(datetime.datetime.now().second)+"_"+ str(datetime.datetime.now().microsecond)

def CreateResponse(Message):
    import socket
    import datetime

    def Time():
        return str(datetime.datetime.now().minute) + "_" + str(datetime.datetime.now().second) + "_" + str(
            datetime.datetime.now().microsecond)

    #host = 'ofd.uc-itcom.ru'
    #port = 12654

    #host='kkm-server-test.1-ofd.ru'
    #port = 7777

    host = 'localhost'
    port = 12000

    sock = socket.socket()
    sock.connect((host, port))

    sock.send(Message)
    data = sock.recv(1024)
    print('ok')
    f = open("saved/" + Time() + "cli", "wb")
    f.write(data)
    sock.close()
    return(data)

def Accept():
    conn, addr = sock.accept()

    print ('connected:')
    global N
    while True:
        data = conn.recv(1024)
        if not data:
            break
        response = CreateResponse(data)
        print(response)
        conn.send(response)

        f = open("saved/"+ Time()+"srv", "wb")
        f.write(data)
    conn.close()


while True:
    Accept()




