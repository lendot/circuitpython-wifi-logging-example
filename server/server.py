import time
from flask import Flask,request
import csv


# where to store the data. We'll use a csv file
LOG_FILE = "data.csv"


def create_app(test_config = None, prod = True):
    """ application factory; creates and initializes the server """

    # where to store the data. We'll use a csv file. Change the name as needed
    LOG_FILE = "data.csv"


    app = Flask(__name__)

    # put server initialization code here (log file setup, db connections, etc)

    # initialize the csv file for storing data
    print(f'Writing data to {LOG_FILE}')
    
    with open(LOG_FILE,'w') as logfile:
        csv_writer = csv.writer(logfile,delimiter=',')
        csv_writer.writerow(['timestamp','x','y','z'])

    app.config.update(
            LOG_FILE = LOG_FILE 
    )

    """
    This is the listener for the root URL of the server (http://[server_address]/)
    It isn't used for anything here, but it's good to at least have a placeholder. 
    """
    @app.route("/")
    def index():
        return "<p>Hello, World! This is an example server</p>"

    """
    This is the URL that logging data will be sent to. (http://[server_address]/log)
    It supports both GET and POST mmethods, so the devices can use either of those.
    GET is fine for starters and is a little easier to debug, but if the data being
    sent starts getting complex, it might make more sense to switch to POST
    """
    @app.route("/log",methods=['GET','POST'])
    def log():

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

        timestamp = time.strftime("%H:%M:%S", time.localtime())
             
        print(f'({timestamp},{x},{y},{z})')

        # put the data in the csv file
        logfile = app.config['LOG_FILE']
        with open(logfile,'a') as csv_file:
            csv_writer = csv.writer(csv_file,delimiter=',')
            csv_writer.writerow([timestamp,x,y,z])


        return "logging complete"

    return app


if __name__ == "__main__":
    # initialize the server
    app = create_app()
    # run the server so that it accepts connections from any any address
    app.run(host="0.0.0.0")

