import socket
import threading


class TCPclient:
    def __init__(self):
        self.quit = False

    def recieve(self, client):
        while not self.quit:
            try:
                rcvd = client.recv(1024)
                print('Recieved:' + rcvd.decode())
                if rcvd == b'exit':
                    print('your friend left the chat!\nenter exit to leave the chat\n')
                    self.quit = True
                    client.close()
                    return 0
            except:
                exit(0)

    def send(self, client):
        while not self.quit:
            try:
                msg = input('send: \n')
                client.send(msg.encode())
                if msg == 'exit':
                    print('closed')
                    self.quit = True
                    client.close()
                    return 0
            except:
                exit(0)

    def startChat(self, addr):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((addr[0], int(addr[1])))
        print('conected!')

        y = threading.Thread(target=TCPclient.send, args=(self, client,))
        x = threading.Thread(target=TCPclient.recieve, args=(self, client,))
        x.start()
        y.start()
        x.join()
        y.join()