from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '김민우 자전거, 나는 지쿠터'
