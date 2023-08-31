# CircuitPython WiFi example

*Note:* This code requires CircuitPython 8 or higher.

Copy `lib/adafruit_requests.mpy` from your CircuitPython library bundle into the
`lib` directory on your CircuitPython device.

Copy `code.py` from this directory to the top level of your CircuitPython device.

Open the `settings.toml` file in that directory (or create it if it doesn't exist)
and add the following lines, editing the values for your environment:

```
WIFI_SSID = "your_wifi_network_name"
WIFI_PASSWORD = "your_wifi_password"
LOGGING_HOST = "your_computer_ip_address"
LOGGING_PORT = 5000
```

When you run the [server](../server), it will tell you what the IP address of your
machine is, which is what you'll use for `LOGGING_HOST`.

