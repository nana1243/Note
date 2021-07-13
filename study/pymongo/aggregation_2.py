# match
# facet
# sort
# group
# addFields
# unwind
# setIntersection
# size
import pprint

from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.test
collection = db.experiments

# $setIntersection
# Takes two or more arrays and returns
# an array that contains the elements that appear in every input array.
# { $setIntersection: [ <array1>, <array2>, ... ] }

aggregation_pipeline = [
    {
        "$project": {
            "A": 1,
            "B": 1,
            "commonToBoth": {"$setIntersection": ["$A", "$B"]},
            "_id": 0,
        }
    }
]

res1 = list(db.experiments.aggregate(aggregation_pipeline))
pprint.pprint(res1)

# $size
# Counts and returns the total number of items in an array.

aggregation_pipeline = [
    {
        "$project": {
            "item": 1,
            "numberOfColors": {
                "$cond": {
                    "if": {"$isArray": "$colors"},
                    "then": {"$size": "$colors"},
                    "else": "NA",
                }
            },
        }
    }
]

res2 = list(db.inventory.aggregate(aggregation_pipeline))
pprint.pprint(res2)

# $unwind
# Deconstructs an array field from the input
# documents to output a document for each element.
# Each output document is the input document with the
# value of the array field replaced by the element.
res3 = list(db.inventory.aggregate([{"$unwind": "$sizes"}]))
print(res3)

# facet
# The $facet stage allows you to create
# multi-faceted aggregations which characterize
# data across multiple dimensions, or facets,
# within a single aggregation stage.

res4 = db.artwork.aggregate(
    [
        {
            "$facet": {
                "categorizedByTags": [
                    {"$unwind": "$tags"},
                    {"$sortByCount": "$tags"},
                ],  # noqa : E501
                "categorizedByPrice": [
                    {"$match": {"price": {"$exists": 1}}},
                    {
                        "$bucket": {
                            "groupBy": "$price",
                            "boundaries": [0, 150, 200, 300, 400],
                            "default": "Other",
                            "output": {
                                "count": {"$sum": 1},
                                "titles": {"$push": "$title"},
                            },
                        }
                    },
                ],
                "categorizedByYears(Auto)": [
                    {"$bucketAuto": {"groupBy": "$year", "buckets": 4}}
                ],
            }
        }
    ]
)

print("this is res4!")
pprint.pprint(list(res4))
