"""
Example web server using python and flask

This server listens for HTTP requests on this machine, by default on port 5000,
and writes the data received to a csv file along with a timestamp and ip address.
The data comes as 3 request paramenters, x, y, and z, all of which are assumed
to be floating point numbers.
"""


import time
from flask import Flask,request
import csv


def create_app(test_config = None, prod = True):
    """ application factory; creates and initializes the server """

    # where to store the data. We'll use a csv file. Change as needed. 
    LOG_FILE = "data.csv"


    # create the web app object
    app = Flask(__name__)

    # ==========================================================================
    # put server initialization code here (log file setup, db connections, etc)

    # initialize the csv file for storing data
    print(f'Writing data to {LOG_FILE}')
    with open(LOG_FILE,'w') as logfile:
        csv_writer = csv.writer(logfile,delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(['timestamp','ip','x','y','z'])


    # put the log file location into the application config so that other parts
    # of the app can access it
    app.config.update(
            LOG_FILE = LOG_FILE 
    )

    # end server initialization code
    # ==========================================================================

    @app.route("/")
    def index():
        """
        This is the listener for the root URL of the server (http://[server_address]/)
        It isn't used for anything here, but it's good to at least have a placeholder there. 
        """
        return "<p>Hello, World! This is an example server</p>"


    @app.route("/log",methods=['GET','POST'])
    def log():
        """
        This is the URL that logging data will be sent to (http://[server_address]/log).
        """
     
        # get the parameters. In this example they are x, y, and z. Add/change as appropriate
        # for your project 
        x_str = request.args.get('x')
        y_str = request.args.get('y')
        z_str = request.args.get('z')

        # convert paramaters from strings to their native types (in this case, float)
        x = y = z = None
        if x_str is not None:
            x = float(x_str)
        if y_str is not None:
            y = float(y_str)
        if z_str is not None:
            z = float(z_str)

        # get the current time as HH:MM:SS
        timestamp = time.strftime("%H:%M:%S", time.localtime())
             
        # get the client's IP address
        ip_addr = request.remote_addr

        print(f'{timestamp}  {ip_addr}  ({x}, {y}, {z})')

        # Write the data to the csv file.
        logfile = app.config['LOG_FILE']
        with open(logfile,'a') as csv_file:
            csv_writer = csv.writer(csv_file,delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writerow([timestamp,ip_addr,x,y,z])

        """
        What this statement returns is the content that gets sent back to the client.
        In this example, the CircuitPython device only cares about the HTTP status code, so 
        we can just set it to whatever
        """
        return "logging complete"

    return app


if __name__ == "__main__":
    # initialize the server
    app = create_app()
    # run the server so that it accepts connections from any any address
    app.run(host="0.0.0.0")

