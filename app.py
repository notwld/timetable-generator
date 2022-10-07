from flask import Flask, render_template
import json
import webbrowser
from threading import Timer


app = Flask(__name__)
data = json.load(open('data.json', 'r'))

@app.route('/')
def index():
    return render_template('index.html',data=data["data"])

if __name__ == '__main__':
    Timer(1, lambda: webbrowser.open('http://localhost:5000/')).start()
    app.run(debug=True)