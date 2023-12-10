from flask import *

app = flask(__name__)

@app.route("/")
def hello():
    return "He!"

if __name__ == "__main__":
    app.run(debug=True)
