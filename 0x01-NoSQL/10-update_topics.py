#!/usr/bin/env python3
"""
this module is to define a Python function that changes all
topics of a school document based on the name
"""


def update_topics(mongo_collection, name,  topics):
    """
    Change topics of a school document based on the name
    """
    q = {"name": name}
    u = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(q, u)
