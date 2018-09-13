import pickle
import numpy as np  # Pickle uses this
from flask import request, jsonify

from app import app, db, ann_ix
from app.models import Vector


class InvalidUsage(Exception):

    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return 'Ok'


@app.route('/add', methods=['POST'])
def add_vector():
    data = request.get_json()

    if 'vector' not in data:
        raise InvalidUsage('Vector parameter is missing')

    vector = data['vector']

    print(vars(app.config))
    if len(vector) != app.config['ANN_INDEX_LENGTH']:
        raise InvalidUsage('Vector has the wrong length')

    entry = Vector(vector=vector)
    db.session.add(entry)
    db.session.commit()
    return jsonify({'index': entry.id})


@app.route('/find', methods=['POST'])
def find_vector():
    data = request.get_json()
    if 'vector' not in data:
        raise InvalidUsage('Vector parameter is missing', status_code=400)
    vector = data['vector']
    match = ann_ix.get_nns_by_vector(vector, 1, search_k=-1, include_distances=True)

    if len(match[0]) > 0:
        result = {'index': match[0][0], 'distance': match[1][0]}
        return jsonify(result)
    return jsonify({'index': None, 'distance': None})
