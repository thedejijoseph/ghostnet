import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 80))

server.listen(3)
conn, addr = server.accept()
print(addr)
server.close()
