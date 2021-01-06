import socketserver

class TCPRequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        self.name = self.request.recv(1024)
        print(self.name.decode()+" is connected")

        self.request.sendall(("hi "+self.name.decode()).encode())


    def handle(self):
        while(1):
            self.data = self.request.recv(1024)
            if(self.data.decode() == "1" or self.data == b''):
                break

            # print("test")
            print(self.name.decode()+" : "+self.data.decode())

            print("you: ", end="")
            reply = input()
            self.request.sendall(reply.encode())



with socketserver.TCPServer(("localhost", 8001), TCPRequestHandler) as server:
    server.serve_forever()


