from typing import List

import bson
from pydantic import BaseModel as PydanticBaseModel
from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("localhost", 27017)
db = client.test


class BaseModel(PydanticBaseModel):
    class Config:
        json_encoders = {bson.ObjectId: str}
        allow_population_by_field_name = True
        use_enum_values = True


class SimilarTagFilterQuery(BaseModel):
    query_items: List[str]

    def aggregation(self, field_name: str):
        output_field_name = f"{field_name}"
        res = [
            {"$match": {f"{output_field_name}": {"$in": self.query_items}}},
            {"$unwind": f"${output_field_name}"},
            {
                "$group": {
                    "_id": None,
                    "items": {"$addToSet": f"${output_field_name}"},
                }  # noqa : E501
            },
        ]
        return res


class InventoryRepository:
    __collection__name__ = "inventory"

    def __init__(self, collections: Collection):
        self.collections = collections

    def filter(self, query: SimilarTagFilterQuery):
        res = list(
            self.collections.aggregate(query.aggregation("colors"))
        ).pop()  # noqa : E501
        return res["items"]


test1 = InventoryRepository(db.inventory).filter(
    query=SimilarTagFilterQuery(query_items=["blue"])
)

print(test1)
