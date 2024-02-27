from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/test")
def home():
    return "<p>Test</p>"

if __name__ == '__main__':
    app.run(debug=True)
