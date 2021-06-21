from flask import Flask, jsonify
import logging
import os

app = Flask(__name__)


@app.route("/")
def hello():
    logging.info("Main request successfull")
    app.logger.info("Main request successfull")
    return "Hello World!"


@app.route("/status")
def status():
    logging.info("Status request successfull")
    app.logger.info("Status request successfull")
    return jsonify({"result": "OK - healthy"})


@app.route("/metrics")
def metrics():
    logging.info("Metrics request successfull")
    app.logger.info("Metrics request successfull")

    return jsonify(
        {"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}
    )


if __name__ == "__main__":
    # stream logs to a file
    filename = os.path.join(os.getcwd(), "ram.log")
    logging.basicConfig(filename=filename)
    app.run(debug=True, host="127.0.0.1")
