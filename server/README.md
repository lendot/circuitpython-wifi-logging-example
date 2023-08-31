# Example server

This is a very simple flask-based server that shows how to set up a bare bones logging server.

To set up the server: `pip install -r requirements.txt`

To run the server: `python server.py`

WHen the server starts, you'll see a message something like this:
```
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
* Running on http://10.13.106.21:5000
```
Ignore the ones for 0.0.0.0 and 127.0.0.1; there should be another address, which is the
one your device can use to reach your machine. In this example it's 10.13.106.21, and that's
what would be used for the `LOGGING_HOST` value in the device's `settings.toml`

Data will be logged to `data.csv`
