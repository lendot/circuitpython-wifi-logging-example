import os
import sys
import ipaddress
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


# set up the requests object 
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


"""
The main loop of this program will generate random values of
x, y, and z, send them to the server, sleep for 5 seconds, 
and do the same thing again indefinitely
"""
while True:
    x = random.random() * 10
    y = random.random() * 10
    z = random.random() * 10
    log_url = f'{URL}?x={x}&y={y}&z={z}'
    print(f'request: {log_url}')
    response = requests.get(log_url)
    print(f'response: {response.status_code} {response.reason.decode('utf-8')}') 
    time.sleep(5)

