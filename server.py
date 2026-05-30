"""
考研英语统计 后端
托管 HTML + 读写 data.json
端口: 5060
"""
import json, os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data.json')

@app.route('/')
@app.route('/index.html')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/load', methods=['GET'])
def load():
    if not os.path.exists(DATA_FILE):
        return jsonify({'data': {}})
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return jsonify(json.load(f))

@app.route('/save', methods=['POST'])
def save():
    payload = request.get_json(force=True, silent=True)
    if payload is None:
        return jsonify({'ok': False, 'error': 'invalid JSON'}), 400
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return jsonify({'ok': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5060)
