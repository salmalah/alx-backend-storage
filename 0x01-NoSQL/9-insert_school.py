#!/usr/bin/env python3
"""This module is to define a function to insert into collection"""


def insert_school(mongo_collection, **kwargs):
    """
    insert a documents into collection
    return the new id 
    """
    d = mongo_collection.insert_one(kwargs)
    return d.inserted_id
