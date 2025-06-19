import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12348))

threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

while True:
    msg = input()
    if msg.lower() == 'bye':
        client.send(msg.encode())
        break
    client.send(msg.encode())

client.close()
