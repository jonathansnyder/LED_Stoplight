from flask import Flask, render_template
stoplightctr = Flask(__name__)

@stoplightctr.route('/StoplightControler')
def StoplightControler():
    return render_template('StoplightControler.html')

if __name__ == "__main__":
    stoplightctr.run()