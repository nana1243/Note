import datetime
import pprint

import pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient

# Making a Connection with MongoClient

client = MongoClient("localhost", 27017)

# Getting a Database

db = client.test
collection = db["posts"]

# Inserting a Document
# To insert a document into a collection we can use the `insert_one` method

post = {
    "author": "hennie",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow(),
}
posts = db.posts
post_id = posts.insert_one(post).inserted_id

# print(post_id)
print(db.list_collection_names())

# Getting a Single Document With find_one()
#  It is useful when you know there is only one matching document,
# or are only interested in the first match
# pprint.pprint(posts.find_one({"author":"hennie"}))

# Querying By ObjectId
# None that an ObjectId is not the same as its string representation!
post_id_as_str = str(post_id)
print(f"this is post_id_as_str {post_id_as_str}")
pprint.pprint(posts.find_one({"_id": post_id_as_str}))  # no result!


def get(post_id):
    document = client.db.collection.find_one({"_id": ObjectId(post_id)})
    return document


result = get(post_id_as_str)
print(result)

# Counting!
print(posts.count_documents({}))
print(posts.count_documents({"author": "hennie"}))

# Range Queires

d = datetime.datetime(2021, 2, 1, 12)

for post in posts.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)

# Indexing
# Adding indexes can help accelerate certain queries
# and can also add additional functionality to querying and storing documents.

test = db.profiles.create_index([("user_id", pymongo.ASCENDING)], unique=True)
print(sorted(db.profiles.index_information(())))


user_profiles = [
    {"user_id": 211, "name": "Luke"},
    {"user_id": 212, "name": "Ziltoid"},
]  # noqa : E501

result = db.profiles.insert_many(user_profiles)

new_profile = {"user_id": 213, "name": "Drew"}


# ref ) https://pymongo.readthedocs.io/en/stable/tutorial.html
