import socket

def evaluate_expression(expr):
    try:
        return str(eval(expr))
    except:
        return "Error in expression"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12346))
server_socket.listen(1)
print("Math Server is listening on port 12346...")

while True:
    conn, addr = server_socket.accept()
    print("Connected by", addr)
    expression = conn.recv(1024).decode()
    print("Received expression:", expression)
    result = evaluate_expression(expression)
    conn.send(result.encode())
    conn.close()
