from flask import Flask
#import logging

app = Flask(__name__)

@app.route("/")
def hello():
#    logging.info('Hello World!')
    return "Hello World!"

if __name__ == "__main__":
#    logging.basicConfig(filename='./log/app.log',level=logging.DEBUG)
    app.run(host="0.0.0.0", port=int("5000"))
