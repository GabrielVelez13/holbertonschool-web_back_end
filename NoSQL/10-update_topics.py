#!/usr/bin/env python3
""" Change a collection's document based on a name """


def update_topics(mongo_collection, name, topics):
    """ Updates topics based on a school """
    mongo_collection.update_many({"name":name}, {"$set": {"topics":topics}})
