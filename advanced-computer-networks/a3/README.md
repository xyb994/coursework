# Assignment 3 #

### Program description ###

Python scripts that try to measure the clock offset using the low-latency symmetric link interface between two systems. The scripts also measures the one-way latencies in each direction of the rest of the interfaces.

One server side, the script listening on specified socket port and respond with JSON formated data containing the time request arrives and the time before a response leaves the server. 

On client side, there are two parts: measure clock offset, then use the result to measure one-way latencies.

- **Language** Python

#### Preparation

This program requires Python3

- clone this repository on both `server1` and `server2`

#### Usage

- First, on server side, run `python3 server.py`
- Then, on client side, run `python3 client.py`

##### Sample Output

- server side

```
[___@server1 a3]$ python3 server.py
Server listening on port 39250...
```

- client side

```
[____@server2 a3]$ python3 client.py
===================== enp5s0f0 =====================
The average RTT is 0.27820 ms
The average clock offset is 0.62470 ms
===================== enp5s0f0 =====================
The one-way latency from __1 to __2 is 0.14294 ms
The one-way latency from __2 to __1 is 0.14049 ms
===================== enp5s0f1 =====================
The one-way latency from __1 to __2 is 2.32993 ms
The one-way latency from __2 to __1 is 66.91265 ms
===================== enp5s0f2 =====================
The one-way latency from __1 to __2 is 28.61432 ms
The one-way latency from __2 to __1 is 40.37496 ms
===================== enp5s0f3 =====================
The one-way latency from __1 to __2 is 16.37890 ms
The one-way latency from __2 to __1 is 53.09584 ms
```
