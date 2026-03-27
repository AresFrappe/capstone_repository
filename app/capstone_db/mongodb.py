from app import mongo
from bson.objectid import ObjectId

def get_all_capstones():
    return mongo.db.capstones.find()

def insert_capstone(title, author, year):
    capstone = {
        "title": title,
        "author": author,
        "year": year
    }

    mongo.db.capstones.insert_one(capstone)

    return True

def delete_capstone(capstone_id):
    mongo.db.capstones.delete_one({"_id": ObjectId(capstone_id)})
    return True