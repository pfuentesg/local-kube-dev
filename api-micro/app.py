#!flask/bin/python
import os
import requests
from flask import Flask, jsonify

port = int(os.environ.get("PORT", 5000))
store_service_url = os.environ.get("STORE_SERVICE_URL", "store_service")

app = Flask(__name__)

@app.route('/api/store/<id>', methods=['GET'])
def get_tasks(id):
    uri = 'http://' + store_service_url + '/api/store/' + id
    resp =  requests.get(uri)
    return (resp.text, resp.status_code, resp.headers.items())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)