from flask import flask
stoplightctr = Flask(__name__)

@stoplightctr.route("StoplightControler")
def index():
    return render_template('controlerstyle.html',name=name)

if __name__ == "__main__":
    stoplightctr.run()