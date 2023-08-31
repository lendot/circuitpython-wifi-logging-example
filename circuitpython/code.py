import os
import sys
import ipaddress
import wifi
import socketpool
import board

import adafruit_requests as requests

# load the configuration settings from settings.toml
settings = {} 
settings_keys = ["WIFI_SSID","WIFI_PASSWORD","LOGGING_HOST","LOGGING_PORT"]
for key in settings_keys:
    settings[key] = os.getenv(key)
    if settings[key] is None:
        print(f'Missing {key} setting in settings.toml')
        sys.exit(1)

# URLs to fetch from
HOST = settings["LOGGING_HOST"]
PORT = settings["LOGGING_PORT"] 
TIMEOUT = 5
INTERVAL = 5
MAXBUF = 256

# connect to WiFi 
WIFI_SSID = settings["WIFI_SSID"]
WIFI_PASSWORD = settings["WIFI_PASSWORD"]
print(f'Connecting to {WIFI_SSID}')
wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
print(f'Connected to {WIFI_SSID}')

while True:
    pass

"""
pool = socketpool.SocketPool(wifi.radio)

ipv4 = ipaddress.ip_address(pool.getaddrinfo(HOST, PORT)[0][4][0])

buf = bytearray(MAXBUF)

print("Create TCP Client Socket")
s = pool.socket(pool.AF_INET, pool.SOCK_STREAM)

print("Connecting")
s.connect((HOST, PORT))

PATH="/log"

def get_request(x,y,z):
    # creates an HTTP GET request for the given data
    #
    # :param float x: x value
    # :param float y: y value
    # :param float z: z value
    #
    # This example uses 3 hypothetical float values named x, y, and z. Add/change  as appropriate for your usage
    #

    # create a request of the form "GET /log?x=1.2345&y=2.3456&z=3.4567" 
    request = f'GET {PATH}?x={x}&y={y}&z={z}\n'
    return request


while True:
        #  message with updated values is sent via socket to Pd
        #  all Pd messages need to end with a ";"
        size = s.send(str.encode(' '.join(["x", str(x_map), ";",
                                           "y", str(y_map), ";",
                                           "aX", str(acc_x), ";",
                                           "aY", str(acc_y), ";",
                                           "n", str(note), ";"])))
        #  new_val is reset
        new_val = False

"""
