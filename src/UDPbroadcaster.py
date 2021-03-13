import random
import socket
import time
import datetime
import threading



class UDPbroadcaster:

    def broadcast(self, subnet):

        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Set a timeout so the socket does not block
        # indefinitely when trying to receive data.
        server.settimeout(0.2)
        server.bind(("", 44444))
        message = "Hello"
        message = message.encode()
        startTime = time.time()
        curTime = time.time()
        readyListener = []
        while curTime-startTime < 4 or not readyListener:
            curTime = time.time()
            server.sendto(message, (subnet, 37020))
            print("message sent!")
            time.sleep(1)
            try:
                portAddr = server.recvfrom(1024)
                # print("listenerPort : ", portAddr, "\n")
                readyListener.append(portAddr)
                # print("bade append\n")
            except:
                continue
        selected_port_ddr = readyListener.pop(random.randint(0, len(readyListener)-1))
        # for x in readyListener:
        #     server.sendto("sorry i'm busy now".encode(), (x[1]))
        print("selected : ", selected_port_ddr, "\n")
        return selected_port_ddr[1][0], selected_port_ddr[0]

