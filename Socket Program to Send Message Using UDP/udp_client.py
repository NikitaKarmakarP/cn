import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("You: ")
    client_socket.sendto(message.encode(), ('localhost', 12349))
    if message.lower() == "bye":
        break
    data, _ = client_socket.recvfrom(1024)
    print("Server:", data.decode())

client_socket.close()
