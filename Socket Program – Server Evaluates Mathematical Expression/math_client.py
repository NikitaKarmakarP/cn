import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12346))
expression = input("Enter a math expression (e.g., 3 + 4 * 2): ")
client_socket.send(expression.encode())
result = client_socket.recv(1024).decode()
print("Result from server:", result)
client_socket.close()
