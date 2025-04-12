from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Hello, INDRA!"

if __name__ == '__main__':
    app.run(debug = True)

import os
port = int(os.environ.get("PORT", 5000))
app.run(host = "0.0.0.0", port = port)
