# Assignment 1 #

### Program description ###

#### Preparation

```
virtualenv ENV
source ENV/bin/activate

pip3 install matplotlib
```

#### Run

`python3 simulator.py <arrival rate> <service rate> <duration in second>`

example: `python3 simulator.py 0.7 0.9 600`

A result plot file `simulator-result.pdf` should appear in the same directory.

#### Example Output

```
➜ python3 simulator.py 0.7 0.9 10
0.00000:ARR
        Packet 0 sent to be served, departs at 1.39992
        Next packet arrives at 0.05741
=============================================================
0.05741:ARR
        Packet 1 enqueued, queue length = 1
        Next packet arrives at 3.66820
=============================================================
1.39992:DEP
        Packet 0 departed, spent 1.39992
        Queue length = 0
        Packet 1 sent to be served, departs at 4.78696
        Queue empty
        3.66820:ARR | 10.00000:END | 3.92075:DEP |
=============================================================
3.66820:ARR
        Packet 2 enqueued, queue length = 1
        Next packet arrives at 5.22662
=============================================================
4.78696:DEP
        Packet 1 departed, spent 4.72956
        Queue length = 0
        Packet 2 sent to be served, departs at 5.74722
        Queue empty
        5.22662:ARR | 10.00000:END | 6.93241:DEP |
=============================================================
5.22662:ARR
        Packet 3 enqueued, queue length = 1
        Next packet arrives at 6.07258
=============================================================
5.74722:DEP
        Packet 2 departed, spent 2.07902
        Queue length = 0
        Packet 3 sent to be served, departs at 8.53005
        Queue empty
        6.07258:ARR | 10.00000:END | 6.32866:DEP |
=============================================================
6.07258:ARR
        Packet 4 enqueued, queue length = 1
        Next packet arrives at 7.35954
=============================================================
7.35954:ARR
        Packet 5 enqueued, queue length = 2
        Next packet arrives at 11.33562
=============================================================
8.53005:DEP
        Packet 3 departed, spent 3.30343
        Queue length = 1
        Packet 4 sent to be served, departs at 12.05821
        Queue length = 1
       11.33562:ARR | 10.00000:END | 13.71466:DEP |
=============================================================
11.33562:ARR
        Packet 6 enqueued, queue length = 2
        Next packet arrives at 11.54982
=============================================================
10.00000:END
Simulation done at 10.0, Events: 11, Arrivals: 7, Departures: 4
```
