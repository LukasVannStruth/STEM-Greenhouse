from flask import Flask, render_template
import data
import logging
app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.DEBUG)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)