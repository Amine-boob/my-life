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




# sophesticated vrsion :

# server side 
import socket 
import threading 
import concurrent.futures

def handle_client(c):
    while True :
        data = c.recv(1024).decode()
        if data :
            print(f"the data from the client is : {data}")
            c.send("you send a message !".encode())
        else :
            c.close()
            break


def main():
    host = "127.0.0.1"
    port = 9090
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(5)
    while True :
        communicate ,address = server.accept()
        for _ in range(5) :
           threading.Thread(target=handle_client ,args=[communicate]).start()

if __name__ == '__main__':
    main()



# client side 
import socket 

host = "127.0.0.1"
port = 9090
name = input("enter your name :")
gh = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

gh.connect((host,port))

while True :
    message = input("enter the data (q to quit):")
    if message == "q" :
        print("goodbye see you later ")
        break
    else :
        gh.send(f"{name} --> {message}".encode("UTF-8"))
        print(gh.recv(1024).decode("UTF-8"))
