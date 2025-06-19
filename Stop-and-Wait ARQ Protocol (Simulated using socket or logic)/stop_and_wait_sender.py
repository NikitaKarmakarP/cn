import socket
import time

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_address = ('localhost', 12350)
sender.settimeout(2)

frames = ['Frame1', 'Frame2', 'Frame3', 'Frame4']
for frame in frames:
    while True:
        sender.sendto(frame.encode(), receiver_address)
        print(f"Sent: {frame}")
        try:
            ack, _ = sender.recvfrom(1024)
            if ack.decode() == f"ACK:{frame}":
                print(f"Received: {ack.decode()}")
                break
        except socket.timeout:
            print("Timeout, resending...")

sender.sendto("END".encode(), receiver_address)
sender.close()
