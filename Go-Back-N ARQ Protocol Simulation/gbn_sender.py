import socket
import time

# Setup
WINDOW_SIZE = 4
TOTAL_FRAMES = 10
TIMEOUT = 2  # seconds

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.settimeout(TIMEOUT)
receiver_address = ('localhost', 12355)

frames = [f"Frame{i}" for i in range(1, TOTAL_FRAMES + 1)]
base = 0
next_seq_num = 0

while base < TOTAL_FRAMES:
    # Send frames in window
    while next_seq_num < base + WINDOW_SIZE and next_seq_num < TOTAL_FRAMES:
        message = f"{next_seq_num}:{frames[next_seq_num]}"
        sender.sendto(message.encode(), receiver_address)
        print(f"Sent: {message}")
        next_seq_num += 1

    # Wait for ACK
    try:
        ack_data, _ = sender.recvfrom(1024)
        ack_num = int(ack_data.decode().split(":")[1])
        print(f"Received ACK for Frame{ack_num}")
        base = ack_num + 1
    except socket.timeout:
        print("Timeout! Resending window...")
        next_seq_num = base  # resend from base

# End communication
sender.sendto("END".encode(), receiver_address)
sender.close()
