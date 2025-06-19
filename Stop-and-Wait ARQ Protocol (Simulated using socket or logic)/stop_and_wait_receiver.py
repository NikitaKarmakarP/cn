import socket

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind(('localhost', 12350))

while True:
    data, addr = receiver.recvfrom(1024)
    frame = data.decode()
    if frame == "END":
        print("Transmission complete.")
        break
    print(f"Received: {frame}")
    receiver.sendto(f"ACK:{frame}".encode(), addr)

receiver.close()
