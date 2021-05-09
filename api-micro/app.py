#!flask/bin/python
import os
import requests
from flask import Flask, jsonify

#Flask default port is 5000 but we can use any other else 
port = int(os.environ.get("PORT", 5000))

#In other namespaces dns will be api-store.default
store_service_url = os.environ.get("STORE_SERVICE_URL", "api-store")


app = Flask(__name__)

@app.route('/api/store/<id>', methods=['GET'])
def get_tasks(id):
    uri = 'http://' + store_service_url + '/api/store/' + id
    # you cannot rreturn the request object
    return requests.get(uri)
    
    # instead we should return the content of the response 
   #resp =  requests.get(uri)
   #return (resp.text, resp.status_code, resp.headers.items())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)