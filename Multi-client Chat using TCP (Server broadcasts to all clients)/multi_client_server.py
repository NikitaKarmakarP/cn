import socket
import threading

clients = []

def handle_client(conn, addr):
    print(f"{addr} connected.")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg.lower() == 'bye':
                break
            print(f"{addr}: {msg}")
            broadcast(f"{addr}: {msg}", conn)
        except:
            break
    conn.close()
    clients.remove(conn)
    print(f"{addr} disconnected.")

def broadcast(msg, connection):
    for client in clients:
        if client != connection:
            client.send(msg.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12348))
server.listen(5)
print("Server running on port 12348...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr)).start()
