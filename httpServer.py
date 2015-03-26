import socket as s
import os.path

BUFF_SIZE = 2048
BIND_ADDRESS =('localhost',8000)
HTTP_OK = """HTTP/1.1 200 OK\nContent-Type: text/html\n\n\n"""

if __name__ == "__main__":
    socket = s.socket()
    socket.bind(BIND_ADDRESS)
    socket.listen(10)
    while True:
        c,a = socket.accept()
        buff = c.recv(BUFF_SIZE)
        filePath = ''
       
        res = buff.split('\n')[0].split(' ')[1]
        filePath = './' + res  
        if not os.path.isfile(filePath):
            filePath ='./index.html' 

        fd = open(filePath,'r')
        fileContent = HTTP_OK + fd.read()
        c.send(fileContent)
        fd.close()
        c.close()
    socket.close()
            
