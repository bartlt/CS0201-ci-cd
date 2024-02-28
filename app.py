from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/test")
def home():
    return "<p>Test Server</p>"

@app.route("/info")
def home():
    import os
    return os.uname()

if __name__ == '__main__':
    app.run(debug=True)
