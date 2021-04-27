from flask import Flask
from flask import request
from hildebrand import Glow

app = Flask(__name__)
glow = Glow()

@app.route('/metrics')
def Main():
    return(
      "timestamp " + str(glow.getElecCurrent['data'][0][0]) + "\nconsumption " + str(glow.getElecCurrent['data'][0][1]))

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")