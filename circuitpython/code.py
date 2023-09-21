import os
import sys
import wifi
import socketpool
import board
import time
import gc
import random
import adafruit_requests

# load the configuration settings from settings.toml
settings = {} 
settings_keys = ["WIFI_SSID","WIFI_PASSWORD","LOGGING_HOST","LOGGING_PORT"]
for key in settings_keys:
    settings[key] = os.getenv(key)
    if settings[key] is None:
        print(f'Missing {key} setting in settings.toml')
        sys.exit(1)

# URL construction info 
HOST = settings["LOGGING_HOST"]
PORT = settings["LOGGING_PORT"] 
PATH="/log"
URL = f'http://{HOST}:{PORT}{PATH}'
print(f'Base URL is {URL}')


# set up the requests object for making HTTP requests
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool)


# connect to WiFi 
WIFI_SSID = settings["WIFI_SSID"]
WIFI_PASSWORD = settings["WIFI_PASSWORD"]
print(f'Connecting to {WIFI_SSID}')
while not wifi.radio.ipv4_address:
    try:
        wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
    except ConnectionError as e:
        print("Connection Error:", e)
        print("Retrying in 10 seconds")
        time.sleep(10)
        gc.collect()
print("Connected!\n")

print(f'IP Address: {wifi.radio.ipv4_address}')
print(f'Subnet    : {wifi.radio.ipv4_subnet}')
print(f'Gateway   : {wifi.radio.ipv4_gateway}')
print(f'RSSI      : {wifi.radio.ap_info.rssi}')
print("")



"""
The main loop of this program generates random values for 3 variables, x, y, and z, 
and sends them to the server. It then sleeps for 5 seconds and repeats indefinitely
"""
while True:
    x = random.random() * 10
    y = random.random() * 10
    z = random.random() * 10

    # this is what gets sent to the server
    log_url = f'{URL}?x={x}&y={y}&z={z}'
    print(f'request: {log_url}')

    # send the request to the server
    response = requests.get(log_url)

    # this is what comes back from the server under normal circumstances it should
    # be 200 OK
    print(f'response: {response.status_code} {response.reason.decode('utf-8')}') 

    time.sleep(5)

