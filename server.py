import socket
import thread
import hashlib

serversock = socket.socket()
host = socket.gethostname();
port = 9000;
serversock.bind((host,port));
filename = ""
serversock.listen(10);
print "Waiting for a connection....."

clientsocket,addr = serversock.accept() 
print("Got a connection from %s" % str(addr))
while True:
    size = clientsocket.recv(1)
    filesz = clientsocket.recv(1)
    if filesz.isdigit():
        size += filesz
        filesize = int(size)
    else:
        filesize = int(size)    
    print filesize
    for i in range(0,filesize):
        if filesz.isdigit():
            filename += clientsocket.recv(1)
        else:
            filename += filesz
            filesz = "0"
    print filename      
    file_to_write = open(filename, 'wb')
    while True:
        data = clientsocket.recv(1024)
        #print data
        if not data:
            break
        file_to_write.write(data)
    file_to_write.close()
    print 'File received successfully'
serversock.close()
