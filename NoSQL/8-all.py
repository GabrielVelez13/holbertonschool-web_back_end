#!/usr/bin/env python3
""" List all documents in a collection using pyMongo """
import pymongo

def list_all(mongo_collection):
    data = mongo_collection.find()
    return list(data) if data else []
