# Day 29: REST API with Flask + MongoDB   (pip install flask pymongo)
# Run: python quickstart/day_29.py   then in another terminal:
#   curl -X POST -H "Content-Type: application/json" -d '{"name":"Ana"}' localhost:5000/api/v1/students
#   curl localhost:5000/api/v1/students
import os

from bson.objectid import ObjectId
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
db = MongoClient(os.environ.get('MONGODB_URI', 'mongodb://localhost:27017'))['school']


def clean(doc):
    doc['_id'] = str(doc['_id'])              # ObjectId -> str so it fits in JSON
    return doc


@app.route('/api/v1/students', methods=['GET'])
def list_students():
    return jsonify([clean(s) for s in db.students.find()])


@app.route('/api/v1/students/<id>', methods=['GET'])
def get_student(id):
    doc = db.students.find_one({'_id': ObjectId(id)})
    if doc is None:
        return jsonify(error='not found'), 404
    return jsonify(clean(doc))


@app.route('/api/v1/students', methods=['POST'])
def create_student():
    new_id = db.students.insert_one(request.get_json()).inserted_id   # request body -> dict
    return jsonify(_id=str(new_id)), 201


@app.route('/api/v1/students/<id>', methods=['PUT'])
def update_student(id):
    db.students.update_one({'_id': ObjectId(id)}, {'$set': request.get_json()})
    return jsonify(clean(db.students.find_one({'_id': ObjectId(id)})))


@app.route('/api/v1/students/<id>', methods=['DELETE'])
def delete_student(id):
    db.students.delete_one({'_id': ObjectId(id)})
    return '', 204                            # 204 = done, nothing to send back


if __name__ == '__main__':
    app.run(debug=True)
