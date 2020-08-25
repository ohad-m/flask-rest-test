from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    print(json.loads(request.data)['a'])
    return 'Hello, World!'

app.run(debug=True)