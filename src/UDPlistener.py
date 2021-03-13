import socket
import random
import time

class UDPlistener:

    def listen(self,ip):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        client.bind((ip, 37020))
        while True:
            rcvd, addr = client.recvfrom(1024)
            print("received message: ", rcvd.decode())
            if len(rcvd) != 0:
                if rcvd.decode() == "rejected": ##
                    print("rejected!\n")
                    exit(0) ##
                port = random.randrange(1000, 5000)
                message = str(port)
                message = message.encode()
                client.sendto(message, addr)
                client.sendto(message, addr)
                return port