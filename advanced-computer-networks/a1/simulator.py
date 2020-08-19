import sys
import time
import random
import matplotlib.pyplot as plt
from queue import PriorityQueue, Queue


event_queue = PriorityQueue()
waiting_queue = Queue()

arrival_rate = float(sys.argv[1])
service_rate = float(sys.argv[2])
duration = float(sys.argv[3])

event_count = 0
arrival_count = 0
departure_count = 0

next_arrival = 0.0
next_departure = 0.0

event_queue.put((next_arrival, "ARR"))

# time tracking
start_time = time.time()
end_time = start_time + duration
simulator_time = 0

while start_time + simulator_time < end_time:
    event = event_queue.get()  # removes the earliest event from the queue
    event_count += 1
    simulator_time = event[0]  # sets simulator time to the time of the event
    event_type = event[1]
    print('{0:.5f}:{1}'.format(simulator_time, event_type))

    # routes the execution
    if event_type == "ARR":
        # schedule the next packet arrival event
        next_arrival += random.expovariate(arrival_rate)
        if event_queue.empty():  # serve the packet
            next_departure = next_arrival + random.expovariate(service_rate)
            print("        Packet {0} sent to be served, departs at {1:.5f}"
                  .format(arrival_count, next_departure))
            event_queue.put((next_departure, "DEP", event[0]))
        elif event_queue.full():  # drop the packet
            print(">.< queue is full")
            continue
        else:  # enqueue the packet
            waiting_queue.put((arrival_count, event[0]))
            print("        Packet {0} enqueued, queue length = {1}"
                  .format(arrival_count, waiting_queue.qsize()))

        event_queue.put((next_arrival, "ARR"))
        print("        Next packet arrives at {0:.5f}".format(next_arrival))
        print("=============================================================")

        arrival_count += 1
    elif event_type == "DEP":
        print("        Packet {0} departed, spent {1:.5f}"
              .format(departure_count, event[0] - event[2]))

        if not event_queue.empty():  # if queue is not empty
            waiting_item = waiting_queue.get() # remove the the head waiting q
            print("        Queue length = {}".format(waiting_queue.qsize()))
            # schedule the packet departure event
            next_departure = next_arrival + random.expovariate(service_rate)
            event_queue.put((next_departure, "DEP", waiting_item[1]))
            print("        Packet {0} sent to be served, departs at {1:.5f}"
                  .format(waiting_item[0], next_departure))

            if waiting_queue.empty():
                print("        Queue empty")
            else:
                print("        Queue length = {}"
                      .format(waiting_queue.qsize()))

        next_departure = next_arrival + random.expovariate(service_rate)

        print("{0:15.5f}:ARR | {1:.5f}:END | {2:.5f}:DEP |"
              .format(next_arrival, duration, next_departure))
        print("=============================================================")
        departure_count += 1

print("{0:.5f}:END".format(duration))
print("Simulation done at {0:.1f}, Events: {1}, Arrivals: {2}, Departures: "
      "{3}".format(duration, event_count, arrival_count, departure_count))

# plot
f = plt.figure(figsize=(5.5,4))
plt.xlabel("Load")
plt.ylabel("Residency Time")
plt.title("M/M/1 Queuing System Simulation vs Theoretical")
plt.xlim(0, 1)
plt.ylim(0, 20)

f, ax = plt.subplots()
ax.plot()

# plt.plot(x, x)
# plt.plot(x, 2 * x)

plt.legend(['Simulation', 'Theoretical'], loc='upper left')

plt.show()
f.savefig("simulator-result.pdf", bbox_inches='tight')
