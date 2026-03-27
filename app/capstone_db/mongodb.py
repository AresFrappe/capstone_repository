from flask import current_app
from bson.objectid import ObjectId

def get_mongo():
    return current_app.extensions["pymongo"]

## no logic for now