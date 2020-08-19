import socket
import time
import json

HOST = ''
PORT = 25006

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)

while True:
  conn, addr = s.accept()
  arrival_time = time.time()

  print(addr)

  send_time = time.time()
  data = json.dumps({"t2": arrival_time, "t3": send_time})

  conn.sendall(data.encode())
  conn.close()
