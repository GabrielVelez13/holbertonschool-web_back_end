#!/usr/bin/env python3
""" Checks the status of logs """
from pymongo import MongoClient

""" Counts all the methods """
client = MongoClient('mongodb://localhost:27017/')
col = client.logs.nginx

totalLogs = col.count_documents({})
print(f"{totalLogs} logs")

print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    print(f"\tmethod {method}: {col.count_documents({"method": method})}")

count = col.count_documents({"method": "GET", "path": "/status"})
print(f"{count} status check")
