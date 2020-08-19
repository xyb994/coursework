import socket
import time
import json

PORT = 39250

s = socket.socket()
s.bind(("", PORT))
s.listen(1)
print(f"Server listening on port {PORT}...")

while True:
    conn, addr = s.accept()
    arrival_time = time.time()

    # print(f"Accepting connection from {addr}")

    send_time = time.time()
    data = json.dumps({"t2": arrival_time, "t3": send_time})

    conn.sendall(data.encode())
    conn.close()
