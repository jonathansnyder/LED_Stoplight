from flask import flask
stoplightctr = Flask(__name__)

@stoplightctr.route("StoplightControler")
def index():
    return "Control the light!"

if __name__ == "__main__":
    stoplightctr.run()