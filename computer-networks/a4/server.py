import time
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/servertime')
def servertime():
  arrival_time = int(time.time() * 1000)
  send_time = int(time.time() * 1000)

  response = jsonify({"t2": arrival_time, "t3": send_time})

  return response

@app.route('/time.html')
def send_clock_offset_page():
    return send_from_directory('', 'time.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=25004)
