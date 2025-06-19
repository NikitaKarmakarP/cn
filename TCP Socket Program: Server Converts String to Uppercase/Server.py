# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening on port 12345...")

while True:
    conn, addr = server_socket.accept()
    print("Connected by", addr)
    data = conn.recv(1024).decode()
    if not data:
        break
    response = data.upper()
    conn.send(response.encode())
    conn.close()
