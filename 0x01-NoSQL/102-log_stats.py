#!/usr/bin/env python3
"""
this module is define script that provides some stats about Nginx logs stored in MongoDB
"""


def print_logs_stats(collection):
    """
    Provides improved stats about Nginx logs stored in MongoDB
    """
    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")
    ip_counts = Counter(log["ip"] for log in collection.find({}, {"ip": 1}))
    top_ips = ip_counts.most_common(10)

    print("IPs:")
    for ip, count in top_ips:
        print(f"    {ip}: {count}")
