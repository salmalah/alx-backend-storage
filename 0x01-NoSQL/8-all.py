#!/usr/bin/env python3
"""
This module is to define a Python function that lists
all documents in a collection
"""


def list_all(mongo_collection):
    """
    declare function
    return : List off documment in a collection
    """
    docs = mongo_collection.find()
    return docs
