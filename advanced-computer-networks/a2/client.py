import sys
import time
import requests

REPETITION = 200

if len(sys.argv) < 3:
    print("Usage: python3 client.py <SERVER_IP> <PORT>")
    sys.exit()

SERVER_IP = sys.argv[1]
HTTP_PORT = sys.argv[2]

REQUEST_FILE_URL = f"http://{SERVER_IP}:{HTTP_PORT}/file"

total_download_count = 0
prediction_success_count = 0
total_time = 0
actual_download_duration = 0
predicted_download_duration = 1
total_offset = 0 # total actual and average download duration offset

for i in range(REPETITION):
    start_time = time.time()
    r = requests.get(url=REQUEST_FILE_URL)
    end_time = time.time()

    total_download_count += 1
    actual_download_duration = end_time - start_time
    total_time += actual_download_duration

    if actual_download_duration < predicted_download_duration:
        prediction_success_count += 1

    correct_prediction_ratio = prediction_success_count / total_download_count

    print(total_download_count)
    print(f"predicted download duration = {predicted_download_duration:.5f}")
    print(f"actual download duration = {actual_download_duration:.5f}")
    print(f"current correct prediction rate = {correct_prediction_ratio:.2f}")
    print("=======================================")

    average_duration = total_time / total_download_count
    total_offset += actual_download_duration - average_duration
    predicted_download_duration = average_duration\
        + 3 * abs(total_offset / total_download_count)

print(f"Time Elapsed = {total_time:.5f} seconds")
print(f"Download Count = {total_download_count}")
print(f"Correct Prediction / Total Run = {correct_prediction_ratio}")
