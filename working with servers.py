# server side :
import socket

#host = socket.gethostbyname(socket.gethostname()) #to get your loopback ip 
host = "192.168.1.153" 
port = 9090

# this socket is just for acception connection 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))

# to accept 5 people then reject the other people 
server.listen(5)

# for each connection we get a new socket that allows us to communicate with that client 
while True :
    # when a client try to connect to that server , the accept method trigger ,
    # and return the addres of that client and a socket that we use use to communicate with that client
    communication_socket , address = server.accept()
    print(f"connected to {address}")
    message = communication_socket.recv(1024).decode("UTF-8")
    print(f"the message from the client is :{message}")
    communication_socket.send(f"got your message !".encode("UTF-8"))
    communication_socket.close()
    print("connection with the client terminate !")




# client side :
import socket 

host = "192.168.1.153"
port = 9090

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect((host,port))
socket.send("hello world".encode("UTF-8"))
print(socket.recv(1024).decode("UTF-8"))

