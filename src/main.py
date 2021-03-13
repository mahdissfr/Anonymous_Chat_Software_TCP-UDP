
from UDPbroadcaster import UDPbroadcaster
from UDPlistener import UDPlistener
from TCPserver import TCPserver
from TCPclient import TCPclient


decision = input("1.want to start a chat\n"
                 "2.wait for a request\n")

ip = input("enter your ip address\n")
if decision == "1":
    four = ip.split(".")
    subnet = four[0]+"."+four[1]+"."+four[2]+".255"
    broadcaster = UDPbroadcaster()
    addrport = broadcaster.broadcast(subnet)
    tcp = TCPclient()
    print("enter 'exit' to leave the chat\n")
    tcp.startChat(addrport)
if decision == "2":
    listener = UDPlistener()
    port = listener.listen(ip)
    tcp = TCPserver()
    print("enter 'exit' to leave the chat\n")
    tcp.startChat(port)
