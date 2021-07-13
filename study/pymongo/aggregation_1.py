from typing import List, Optional

from pydantic import BaseModel
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.test
collection = db["posts"]

POST_PARAM_TO_FIELD = {
    "authors": "author",
}
PARAM_TO_FIELD = {
    "authors": "authors",
    "tags": "tags",
}


class PostFilterQuery(BaseModel):
    authors: List[str]
    tags: Optional[List[str]]

    page: int = 1
    per_page: int = 20

    def aggregation(self):
        match_pipeline = self.match_pipeline()
        add_pipeline = self.add_field_pipeline()
        print(match_pipeline)
        print(add_pipeline)

    def match_pipeline(self) -> Optional:
        in_query = self._in_query()
        # [{'author': {'$in': ['hennie', 'Mike']}}]
        return in_query

    def _in_query(self):
        fields = {"authors"}
        params = self.dict(
            include=fields, exclude_none=True
        )  # {'authors': ['hennie', 'Mike']}
        if not params:
            return None
        return [
            {POST_PARAM_TO_FIELD[field]: {"$in": values}}
            for field, values in params.items()
        ]

    def add_field_pipeline(self):
        def _set_intersection(_values, _field):
            print(_values, _field)
            return {"$size": {"$$setIntersection": [_values, f"${_field}"]}}

        def _in(_values, _field):
            return {"$toInt": {"$in": [f"${_field}", _values]}}

        fields_to_expression = {"authors": _set_intersection, "tags": _in}

        params = self.dict(
            include=set(fields_to_expression.keys()), exclude=None
        )  # noqa : E501
        print(params)
        pipeline = {
            "$addFields": {
                f"matched_{param}": fields_to_expression[param](
                    values, PARAM_TO_FIELD[param]
                )
                for param, values in params.items()
            }
        }
        print(pipeline)
        if not params:
            return None
        return pipeline


qry = PostFilterQuery(
    authors=["hennie", "Mike"], tags=["python"]
).aggregation()  # noqa : E501
