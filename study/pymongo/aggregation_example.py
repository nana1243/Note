import pprint

from bson.son import SON
from pymongo import MongoClient

# Aggregation FrameWork
# this example shows how to use the aggregate() method
# to use the aggregation frame_work

db = MongoClient().test
result = db.recommendation.insert_many(
    [
        {"user_id": 1, "priorities": 2, "score": 20, "play_list_id": 33},
        {"user_id": 2, "priorities": 2, "score": 20, "play_list_id": 33},
        {"user_id": 3, "priorities": 2, "score": 20, "play_list_id": 33},
        {"user_id": 4, "priorities": 2, "score": 20, "play_list_id": 33},
    ]
)

pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
]

pprint.pprint(list(db.things.aggregate(pipeline)))


# https://pymongo.readthedocs.io/en/stable/examples/aggregation.html?highlight=aggregation
# https://docs.mongodb.com/manual/core/aggregation-pipeline/
