from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/codec')
def hello(name=None):
    return render_template('decoder.html')
