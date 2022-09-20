import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

def get_response(url, token=None):
    params = {}
    if token:
        params = {"token":token}
    response = requests.get(url, params=params)
    parsed_response = response.json()
    return parsed_response

parsed_response = get_response(url)
token = parsed_response["token"]
seconds = parsed_response["seconds"]

parsed_response = get_response(url, token)
status = parsed_response["status"]
is_not_ready_status = "Job is NOT ready"
if status == is_not_ready_status:
    print("OK not ready")
else:
    print("NO not ready")

time.sleep(seconds)

parsed_response = get_response(url, token)
status = parsed_response["status"]
result = parsed_response["result"]
is_ready_status = "Job is ready"
if status == is_ready_status and result:
    print("OK ready")
else:
    print("NO ready")



