import socket

soc = socket.socket()
soc.connect(("localhost", 8001))

print("connected, press 1 for disconnecting")

print("Type your identity: ")

while(1):
    data = input("You: ")  #blocking call  

    soc.sendall(data.encode()) # "b'" is converting string into an object of byte class to prevent omission of data. 
    #https://docs.python.org/3/library/stdtypes.html?highlight=bytes#bytes

    if(data == "1"):
        break


    data = soc.recv(1024)
    print("Server: "+data.decode())

