from flask import Flask, jsonify, request
import random
import datetime as dt
from uuid import uuid4

app = Flask(__name__)


@app.before_first_request
def generate_key():
    return str(uuid4())


secret = generate_key()


@app.route("/temp/")
def foo():
    key = request.args.get("key")

    if key is None:
        return jsonify({
            "error": "Must specify key parameter."
        })
    elif key == secret:
        return jsonify({
            "metadata": {
                "request_time": dt.datetime.now()
            },
            "data": {
                "temp": random.randint(10, 100)
            }
        })
    else:
        return jsonify({
            "error": "Invalid key."
        })


print("Secret is:\t{}".format(secret))
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80)