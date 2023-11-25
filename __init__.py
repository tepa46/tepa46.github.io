from flask import Flask
from flask import render_template

import os

app = Flask(__name__, template_folder="templates")


@app.route('/')
def start_rendering():
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='127.0.0.1', port=port)
