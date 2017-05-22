from flask import Flask, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return 'Index'



if __name__ == '__main__':
    app.run(debug=True)
