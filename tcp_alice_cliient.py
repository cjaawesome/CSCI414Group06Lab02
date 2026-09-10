# tcp_alice_client.py
#Alice TCP Client

import socket

#Create a TCP socket using IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Set receive buffer size to 4KB
client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)

#Disable Nagle's algorithm
client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

## Connect to Bob's Server and also we change the IP if BOb's server is running on a different machine
client.connect(("127`.0.0.1", 5000))

#Send the required 12 bytes of data to Bob's server
client.sendall(b"Good morning")

#Alice is finished sending, but can still receive BOb's response
client.shutdown(socket.SHUT_WR)

#Recieve Bob's 5-byte response
data = client.recv(5)

#Display Bob's response
print("Bob:", data.decode())

#Close the client socket
client.close()
