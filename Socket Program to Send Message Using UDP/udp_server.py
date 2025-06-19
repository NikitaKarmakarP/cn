import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12349))
print("UDP Server listening on port 12349...")

while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode()
    print(f"Received from {addr}: {message}")
    if message.lower() == "bye":
        print("Connection closed.")
        break
    server_socket.sendto(f"ACK: {message}".encode(), addr)

server_socket.close()
