from decimal import Decimal

from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.test

db.experiments.insert_many(
    [
        {"A": ["red", "blue"], "B": ["red", "blue"]},
        {"A": ["red", "blue"], "B": ["blue", "red", "blue"]},
        {"A": ["red", "blue"], "B": ["red", "blue", "green"]},
        {"A": ["red", "blue"], "B": ["green", "red"]},
        {"A": ["red", "blue"], "B": []},
        {"A": ["red", "blue"], "B": [["red"], ["blue"]]},
        {"A": ["red", "blue"], "B": [["red", "blue"]]},
        {"A": [], "B": []},
        {"A": [], "B": ["red"]},
    ]
)

db.inventory.insert_many(
    [
        {
            "item": "ABC1",
            "description": "product 1",
            "colors": ["blue", "black", "red"],
        },
        {"item": "ABC2", "description": "product 2", "colors": ["purple"]},
        {"item": "XYZ1", "description": "product 3", "colors": []},
        {"item": "ZZZ1", "description": "product 4 - missing colors"},
        {
            "item": "ZZZ2",
            "description": "product 5 - colors is string",
            "colors": "blue,red",
        },
    ]
)

db.inventory.insert_one({"_id": 1, "item": "ABC1", "sizes": ["S", "M", "L"]})

db.artwork.insert_many(
    [
        {
            "_id": 1,
            "title": "The Pillars of Society",
            "artist": "Grosz",
            "year": 1926,
            "price": Decimal("199.99"),
            "tags": ["painting", "satire", "Expressionism", "caricature"],
        },
        {
            "_id": 2,
            "title": "Melancholy III",
            "artist": "Munch",
            "year": 1902,
            "price": Decimal("280.00"),
            "tags": ["woodcut", "Expressionism"],
        },
        {
            "_id": 3,
            "title": "Dancer",
            "artist": "Miro",
            "year": 1925,
            "price": Decimal("76.04"),
            "tags": ["oil", "Surrealism", "painting"],
        },
        {
            "_id": 4,
            "title": "The Great Wave off Kanagawa",
            "artist": "Hokusai",
            "price": Decimal("167.30"),
            "tags": ["woodblock", "ukiyo-e"],
        },
        {
            "_id": 5,
            "title": "The Persistence of Memory",
            "artist": "Dali",
            "year": 1931,
            "price": Decimal("483.00"),
            "tags": ["Surrealism", "painting", "oil"],
        },
        {
            "_id": 6,
            "title": "Composition VII",
            "artist": "Kandinsky",
            "year": 1913,
            "price": Decimal("385.00"),
            "tags": ["oil", "painting", "abstract"],
        },
        {
            "_id": 7,
            "title": "The Scream",
            "artist": "Munch",
            "year": 1893,
            "tags": ["Expressionism", "painting", "oil"],
        },
        {
            "_id": 8,
            "title": "Blue Flower",
            "artist": "O'Keefe",
            "year": 1918,
            "price": Decimal("118.42"),
            "tags": ["abstract", "painting"],
        },
    ]
)
