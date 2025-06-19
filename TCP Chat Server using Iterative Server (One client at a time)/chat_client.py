import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12347))

while True:
    msg = input("You: ")
    client_socket.send(msg.encode())
    if msg.lower() == "bye":
        break
    
    reply = client_socket.recv(1024).decode()
    if reply.lower() == "bye":
        print("Server ended the chat.")
        break
    print("Server:", reply)

client_socket.close()
