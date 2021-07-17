import pprint

from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.test

# $all:

aggregation_pipeline = [
    {
        "$match": {
            "$and": [
                {"item": {"$eq": "ABC1"}},
                {
                    "colors": {
                        "$eq": [
                            "blue",
                        ]
                    }
                },
            ]
        }
    }
]

res1 = list(db.inventory.aggregate(aggregation_pipeline))
pprint.pprint(res1)
