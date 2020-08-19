# Assignment 2 #

### Program description ###

A simple flask server that serves a 1MB file upon request and a simple client side that request file, calculate time it takes to receive the file. After every file download, an estimation for next download is calculated.

- **Platform** macOS/Linux
- **Library** Python Flask

#### Preparation

This program requires Python Flask and requests

- clone the repo on both `__1` and `__2` and do the following
    - create a virtual environment called project_venv `python3 -m venv venv`
    - activate virtual environment `source venv/bin/activate`
    - install Flask and requests `pip install flask requests`

#### Usage

- on server side
  - run `FLASK_APP=server.py flask run --host=<server-ip> [-p port_number]`

- on client side
- run `python3 client.py <server-ip> <server-port>`

##### Example Output

- server side

```
(venv) [____@server1 a2]$ FLASK_APP=server.py flask run --host=10.4.0.1
 * Serving Flask app "server.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://10.4.0.1:5000/ (Press CTRL+C to quit)
10.4.0.2 - - [28/Feb/2019 05:46:47] "GET /file HTTP/1.1" 200 -
10.4.0.2 - - [28/Feb/2019 05:46:47] "GET /file HTTP/1.1" 200 -
10.4.0.2 - - [28/Feb/2019 05:46:47] "GET /file HTTP/1.1" 200 -
10.4.0.2 - - [28/Feb/2019 05:46:48] "GET /file HTTP/1.1" 200 -
10.4.0.2 - - [28/Feb/2019 05:46:48] "GET /file HTTP/1.1" 200 -
10.4.0.2 - - [28/Feb/2019 05:46:51] "GET /file HTTP/1.1" 200 -
10.4.0.2 - - [28/Feb/2019 05:46:51] "GET /file HTTP/1.1" 200 -
10.4.0.2 - - [28/Feb/2019 05:46:51] "GET /file HTTP/1.1" 200 -
10.4.0.2 - - [28/Feb/2019 05:46:52] "GET /file HTTP/1.1" 200 -
```

- client side

```
(venv) [____@server2 a2]$ python3 client.py 10.5.0.1 3925
download count = 1
predicted_duration = 1
actual_duration = 0.08679699897766113
current prediction correct rate = 1.0
=================================
download count = 2
predicted_duration = 0.08679699897766113
actual_duration = 0.06372928619384766
current prediction correct rate = 1.0
=================================
download count = 3
predicted_duration = 0.06834282875061035
actual_duration = 0.04735088348388672
current prediction correct rate = 1.0
=================================
download count = 4
predicted_duration = 0.054794152577718094
actual_duration = 0.08330678939819336
current prediction correct rate = 0.75
=================================
```