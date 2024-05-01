#!/usr/bin/env python3
""" Return a list of schools with a specific topic """


def schools_by_topic(mongo_collection, topic):
    schools = mongo_collection.find({"topics":topic})
    return schools
