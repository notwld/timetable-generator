from flask import Flask, render_template
import json


app = Flask(__name__)
data = json.load(open('data.json', 'r'))

@app.route('/')
def index():
    return render_template('index.html',data=data["data"])

if __name__ == '__main__':
    app.run(debug=True)