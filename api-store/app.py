#!flask/bin/python
import os
from flask import Flask, jsonify
stores = [
    {
        "id": 1,
        "name": "my super store"
    },
     {
        "id": 2,
        "name": "my super store 2"
    }
]
port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

@app.route('/api/store/<id>', methods=['GET'])
def get_tasks(id):
    id = int(id)
    if (len(stores) < id):
        return jsonify({'store':{} })
    return jsonify({'store': stores[id-1]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)