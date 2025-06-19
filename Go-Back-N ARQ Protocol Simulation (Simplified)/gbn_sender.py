import socket
import time

WINDOW_SIZE = 4
frames = [f"Frame{i}" for i in range(1, 11)]

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.settimeout(2)
addr = ('localhost', 12351)

base = 0
next_seq = 0

while base < len(frames):
    while next_seq < base + WINDOW_SIZE and next_seq < len(frames):
        sender.sendto(frames[next_seq].encode(), addr)
        print(f"Sent: {frames[next_seq]}")
        next_seq += 1

    try:
        ack, _ = sender.recvfrom(1024)
        ack_num = int(ack.decode().split("ACK")[1])
        print(f"Received: ACK{ack_num}")
        base = ack_num + 1
    except socket.timeout:
        print("Timeout! Resending window...")
        next_seq = base  # reset and resend from base

sender.sendto("END".encode(), addr)
sender.close()
