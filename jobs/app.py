
from flask import Flask
from flask import render_template

app = Flask("__name__")


@app.route('/')
@app.route('/jobs')
def Jobs():
    return render_template('index.html')
