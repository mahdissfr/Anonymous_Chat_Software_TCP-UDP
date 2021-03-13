import socket
import threading


class TCPserver:
    def __init__(self):
        self.quit = False

    def recieve(self, server, connection):
        while not self.quit:
            try:
                rcvd = connection.recv(1024)
                print('Recieved:' + rcvd.decode())
                if rcvd == b'exit':
                    self.quit = True
                    print('your friend left the chat!\nenter exit to leave the chat\n')
                    server.close()
                    return 0
            except:
                exit(0)

    def send(self, server, connection, address):
        while not self.quit:
            try:
                mess = input('send: \n')
                connection.sendto(mess.encode(), address)
                if mess == 'exit':
                    self.quit = True
                    print('closed')
                    server.close()
                    return 0
            except:
                exit(0)

    def startChat(self, Port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", Port))
        server.listen(1)
        connection , address = server.accept()
        print('conected')

        x = threading.Thread(target=TCPserver.recieve, args=(self, server, connection))
        y = threading.Thread(target=TCPserver.send, args=(self, server, connection, address))
        x.start()
        y.start()
        x.join()
        y.join()

