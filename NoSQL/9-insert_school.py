#!/usr/bin/env python3
""" Inserting data to school """
import pymongo

def insert_school(mongo_collection, **kwargs):
    """ Insert using kwargs into collection """
    if mongo_collection is not None:
        return mongo_collection.insert_one(kwargs).inserted_id
    return None
