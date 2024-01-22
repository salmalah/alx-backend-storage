#!/usr/bin/env python3
"""
this module is define script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
from collections import Counter

def print_logs_stats(collection):
    # Total number of logs
    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    # Methods statistics
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Status check
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

    # IPs statistics
    ip_counts = Counter(log["ip"] for log in collection.find({}, {"ip": 1}))
    top_ips = ip_counts.most_common(10)

    print("IPs:")
    for ip, count in top_ips:
        print(f"    {ip}: {count}")

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    print_logs_stats(collection)

if __name__ == "__main__":
    main()
