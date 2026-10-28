# Day 27: MongoDB   (pip install pymongo)
# Free cluster: mongodb.com/atlas -> Connect -> copy the URI -> export MONGODB_URI="mongodb+srv://..."
import os

from pymongo import MongoClient

client = MongoClient(os.environ.get('MONGODB_URI', 'mongodb://localhost:27017'))
db = client['school']                     # database (created on first insert)
students = db['students']                 # collection = a table of documents (dicts)

students.insert_one({'name': 'Ana', 'age': 17})
students.insert_many([{'name': 'Ben', 'age': 16}, {'name': 'Cy', 'age': 18}])

print(students.find_one({'name': 'Ana'}, {'_id': 0}))     # {'_id': 0} hides the id field
for s in students.find({'age': {'$gt': 16}}, {'_id': 0}).sort('age', -1).limit(2):
    print(s)                              # $gt greater than, -1 = descending

students.update_one({'name': 'Ben'}, {'$set': {'age': 17}})   # $set changes only those fields
students.delete_one({'name': 'Cy'})
print(students.count_documents({}))       # {} = match everything
students.drop()                           # delete the whole collection
