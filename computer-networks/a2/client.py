import socket
import time
import json

HOST = ''
PORT = 25006

rtt_total = 0
clock_offset_total = 0

for i in range(15):
  s = socket.socket()
  send_time = time.time()

  s.connect((HOST, PORT))

  data = s.recv(1024).decode()
  arrival_time = time.time()

  json_data = json.loads(data)
  rtt = (arrival_time - send_time) - (json_data['t3'] - json_data['t2'])
  rtt_total += rtt
  clock_offset_total += send_time + rtt / 2 - json_data['t2']

  s.close()

rtt_average = rtt_total / 15 * 1000
clock_offset_average = clock_offset_total / 15 * 1000

print("The round trip time is " + str(rtt_average) + " ms")
print("The clock offset is " + str(clock_offset_average) + " ms")
