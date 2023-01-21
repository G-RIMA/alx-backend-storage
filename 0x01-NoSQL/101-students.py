#!/usr/bin/env python3
""" pymongo
"""

def top_students(mongo_collection):
    pipeline = [
        {"$unwind": "$scores"},
        {"$group": {"_id": "$_id", "averageScore": {"$avg": "$scores.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
