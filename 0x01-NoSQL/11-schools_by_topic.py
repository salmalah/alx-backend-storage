#!/usr/bin/env python3
"""
This module is the define a Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection,  topic):
    """
    return: the list of schools having a specific topic
    """
    q = {"topics": topic}
    p = {"_id": 1, "name": 1, "topics": 1}
    schools = mongo_collection.find(q, p)
    return schools
