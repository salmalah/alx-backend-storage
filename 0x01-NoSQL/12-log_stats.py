#!/usr/bin/env python3
"""
This module is to define script that provides some
stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Provide some stats about Nginx logs stored in MongoDB
    """
    it = {}
    if option:
        v = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {v}")
        return

    reslt = mongo_collection.count_documents(it)
    print(f"{reslt} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    check_status = mongo_collection.count_documents({"path": "/status"})
    print(f"{check_status} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
