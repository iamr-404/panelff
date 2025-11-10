from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Allowlist Server Running!"})

@app.route('/allowlist', methods=['GET'])
def get_allowlist():
    with open('allowlist.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
