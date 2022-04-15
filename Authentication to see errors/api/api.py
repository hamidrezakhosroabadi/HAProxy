from flask import Flask
app = Flask(__name__)


@app.route('/working')
def working():
    return 'It works'


@app.route('/not-working')
def not_working():
    raise Exception("test")
    return 'Not working :('
