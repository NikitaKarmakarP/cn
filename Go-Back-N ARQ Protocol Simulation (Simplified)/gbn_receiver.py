import socket

expected_frame = 0
receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind(('localhost', 12351))

while True:
    data, addr = receiver.recvfrom(1024)
    frame = data.decode()
    if frame == "END":
        print("All frames received.")
        break
    print(f"Received: {frame}")
    if frame == f"Frame{expected_frame + 1}":
        print(f"Sending ACK{expected_frame}")
        receiver.sendto(f"ACK{expected_frame}".encode(), addr)
        expected_frame += 1
    else:
        print(f"Discarded. Expected Frame{expected_frame + 1}")
        receiver.sendto(f"ACK{expected_frame - 1}".encode(), addr)  # resend last ACK

receiver.close()
