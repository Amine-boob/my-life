# first version (for lerning):

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
    communication_socket , address = server.accept() # this function return two things a new socket that used to communicate woth that client 
                                                     # and it's also return the address of that client that
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



# UDP server (for lerning)
import socket 

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.1",9999))
# we are not going to call 'listen' function or 'accept' function 
# because we are not listening for connection , we are not acception connection 
# we just listening for messages coming 

# that's why we will use 'recvfrom'
message ,address = server.recvfrom(1024) #it return also the address
print(message.decode())
server.sendto("hello client !".encode(),address) #we need to specify to who we will send message to ...



# UDP client  
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


client.sendto("hello server !!".encode() , ("127.0.0.1",9999))
# this function below will return two values in a tuple :(message and the address )
print(client.recvfrom(1024)[0].decode())  # you need to specify only the message !!







# second vrsion :

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








# third version :

# server side
import socket 
import threading 

clients = []
usernames = []
def broadcast(message):
    for client in clients :
        client.send(message)

def handle_client(client):
    while True :
        # try to receive the message from the client if it succeed -->broadcast it to all clients
        try :
            message = client.recv(1024)
            broadcast(message)
        except :
             # if the connection is over we need to remove that client from the list of clients 
            # close the connection to that client 
            index = clients.index(client)
            name = usernames[index] 
            clients.remove(client)
            usernames.remove(name)
            left_message = f"{name} has left the server !"
            broadcast(left_message.encode())
            print(left_message)
            
            client.close()
            break

def main():
    host = "192.168.1.153"
    port = 55558
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(5)
    while True :
        client,address = server.accept()
        print(f"connect to :{address}")
        client.send("USER".encode())
        username = client.recv(1024).decode()
        usernames.append(username)
        clients.append(client)
        
        message = f"{username} :connected to the server "
        print(f"{username} :connected the server")
        broadcast(message.encode())

        threading.Thread(target=handle_client,args=[client]).start()



if __name__ == '__main__':
    main()





# client side 
import socket
import threading 

host = "192.168.1.153"
port = 55558

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
name = input("enter your name :")

def receive():
    while True :
        
        try :
            message = client.recv(1024).decode()
            if message == "USER":
                client.send(name.encode())
            else :
                print(message)
        except :
            print("an issue has accurred !")
            client.close()
            break

def write():
    while True :
        client.send(f"{name} :{input("")}".encode())



threading.Thread(target=receive).start()
threading.Thread(target=write).start()
