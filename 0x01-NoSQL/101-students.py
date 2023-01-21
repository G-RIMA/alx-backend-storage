#!/usr/bin/env python3
""" pymongo
"""
from pymongo import ASCENDING

def top_students(mongo_collection):
    # calculate the average score for each student
    pipeline = [
        {"$group": {"_id": "$student_id", "averageScore": {"$avg": "$score"}}},
        {"$project": {"student_id": "$_id", "averageScore": 1}},
        {"$sort": {"averageScore": ASCENDING}}
    ]
    students = list(mongo_collection.aggregate(pipeline))
    return students
