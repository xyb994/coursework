import socket
import time
import json

PORT = 39250
HOST_0 = "10.5.0.1"
HOSTS = ("10.5.0.1", "10.5.1.1", "10.5.2.1", "10.5.3.1")
REPETITION_0 = 10000
REPETITION = 3000

# find the offset between system clocks
rtt_total = 0
clock_offset_total = 0

for i in range(REPETITION_0):
    s = socket.socket()
    send_time = time.time()

    s.connect((HOST_0, PORT))

    data = s.recv(1024).decode()
    arrival_time = time.time()

    json_data = json.loads(data)
    rtt = (arrival_time - send_time) - (json_data['t3'] - json_data['t2'])
    rtt_total += rtt
    clock_offset_total += send_time + rtt / 2 - json_data['t2']

    s.close()

rtt_average = rtt_total / REPETITION_0 * 1000
clock_offset_average = clock_offset_total / REPETITION_0 * 1000

print(f"The average RTT is {rtt_average:.5f} ms")
print(f"The average clock offset is {clock_offset_average:.5f} ms")

# measures one-way latencies in each direction for the rest of the interfaces
for host in HOSTS:
    server1_to_server2_latency_total = 0
    server2_to_server1_latency_total = 0
    rtt_total = 0

    for i in range(REPETITION):
        s = socket.socket()
        send_time = time.time()

        s.connect((host, PORT))

        data = s.recv(1024).decode()
        arrival_time = time.time()

        json_data = json.loads(data)

        rtt = (arrival_time - send_time) - (json_data['t3'] - json_data['t2'])
        rtt_total += rtt

        server1_to_server2_latency = (arrival_time - json_data['t3']) * 1000 \
            - clock_offset_average
        server1_to_server2_latency_total += server1_to_server2_latency

        server2_to_server1_latency = (json_data['t2'] - send_time) * 1000 \
            + clock_offset_average
        server2_to_server1_latency_total += server2_to_server1_latency

        s.close()

    server1_to_server2_latency_average = server1_to_server2_latency_total / REPETITION
    server2_to_server1_latency_average = server2_to_server1_latency_total / REPETITION

    print(f"===================== enp5s0f{host[-3:-2]} =====================")
    print("The one-way latency from server1 to server2 is "
          f"{server1_to_server2_latency_average:.5f} ms")
    print("The one-way latency from server2 to server1 is "
          f"{server2_to_server1_latency_average:.5f} ms")
