import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12347))
server_socket.listen(1)
print("Chat Server listening on port 12347...")

conn, addr = server_socket.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024).decode()
    if data.lower() == "bye":
        print("Client ended the chat.")
        break
    print("Client:", data)
    
    reply = input("You: ")
    conn.send(reply.encode())
    if reply.lower() == "bye":
        break

conn.close()
server_socket.close()
