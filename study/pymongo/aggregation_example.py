import pprint

from bson.son import SON
from pymongo import MongoClient

# Aggregation FrameWork
# this example shows how to use the aggregate() method
# to use the aggregation frame_work

db = MongoClient().aggregation_example
result = db.things.insert_many(
    [
        {"x": 1, "tags": ["dog", "cat"]},
        {"x": 2, "tags": ["cat"]},
        {"x": 2, "tags": ["mouse", "cat", "dog"]},
        {"x": 3, "tags": []},
    ]
)

print(result.inserted_ids)
pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
]

pprint.pprint(list(db.things.aggregate(pipeline)))


# https://pymongo.readthedocs.io/en/stable/examples/aggregation.html?highlight=aggregation
# https://docs.mongodb.com/manual/core/aggregation-pipeline/
