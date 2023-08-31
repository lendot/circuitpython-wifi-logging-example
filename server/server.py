from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World! This is an example server</p>"

"""
This is the URL that logging data will be sent to. It supports both GET and POST
methods, so the devices can use either of those. GET is fine for starters and is a 
little easier to debug, but if the data being sent starts getting complex, it might
make more sense to switch to POST
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
         
    print(f'({x},{y},{z})')

    return "<p>this is the data logging URL</p>"


if __name__ == "__main__":
    # run the server so that it accepts connections from any any address
    app.run(host="0.0.0.0")
