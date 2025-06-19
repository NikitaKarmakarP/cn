import socket
import time

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.settimeout(2)  # seconds
receiver_address = ('localhost', 12360)

frames = ['Frame1', 'Frame2', 'Frame3', 'Frame4']
seq_num = 0

for frame in frames:
    while True:
        message = f"{seq_num}:{frame}"
        sender.sendto(message.encode(), receiver_address)
        print(f"Sent: {message}")

        try:
            ack, _ = sender.recvfrom(1024)
            ack_seq = int(ack.decode())
            if ack_seq == seq_num:
                print(f"ACK received for seq {ack_seq}")
                seq_num = 1 - seq_num  # Toggle between 0 and 1
                break
        except socket.timeout:
            print("Timeout! Resending frame...")

sender.sendto("END".encode(), receiver_address)
sender.close()
