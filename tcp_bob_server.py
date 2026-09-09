#tcp_bob_server.py
#created with the assistance of ChatGPT
#documented and fixed by Cooper Adcock

import socket
#importing socket package

#create new socket object for ipv4 internet routing
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#set buffer size to 4KB
server.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)

#disable Nagle algorithm
server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

#bind socket to address and port
server.bind(("0.0.0.0", 5000))

#set server to listen mode (accept incoming traffic)
server.listen(1)

#sets socket to accept incoming connection
conn, addr = server.accept()

#receive data from client
data = conn.recv(12)

#print received data
print("Alice:", data.decode())

#send message in return
conn.sendall(b"Hello")

# shut down connection
conn.shutdown(socket.SHUT_WR)

#close connection
conn.close()

#close socket
server.close()