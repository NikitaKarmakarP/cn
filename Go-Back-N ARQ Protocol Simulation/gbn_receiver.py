import socket

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind(('localhost', 12355))

expected_seq = 0

while True:
    data, addr = receiver.recvfrom(1024)
    message = data.decode()
    if message == "END":
        print("Transmission complete.")
        break

    try:
        seq_num, frame_data = message.split(":")
        seq_num = int(seq_num)
    except:
        continue  # skip malformed data

    if seq_num == expected_seq:
        print(f"Received: {frame_data}")
        receiver.sendto(f"ACK:{seq_num}".encode(), addr)
        expected_seq += 1
    else:
        print(f"Discarded: {frame_data}, Expected Frame{expected_seq}")
        # Send ACK for last correctly received frame
        receiver.sendto(f"ACK:{expected_seq - 1}".encode(), addr)

receiver.close()
