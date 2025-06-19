# client.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
message = input("Enter a lowercase string: ")
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
print("Received from server:", data)
client_socket.close()
