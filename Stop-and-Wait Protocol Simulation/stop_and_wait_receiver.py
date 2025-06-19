import socket

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind(('localhost', 12360))

expected_seq = 0

while True:
    data, addr = receiver.recvfrom(1024)
    message = data.decode()

    if message == "END":
        print("Transmission completed.")
        break

    try:
        seq_num, frame = message.split(":")
        seq_num = int(seq_num)
    except:
        continue

    if seq_num == expected_seq:
        print(f"Received: {frame} | Seq: {seq_num}")
        receiver.sendto(str(seq_num).encode(), addr)
        expected_seq = 1 - expected_seq  # Toggle
    else:
        print(f"Duplicate frame ignored: {frame}")
        receiver.sendto(str(1 - expected_seq).encode(), addr)

receiver.close()
