#!/usr/bin/env python3
"""
this module is the define a Python function that returns all students sorted by average score
"""


def top_students(mongo_collection):
  """
  return list of students
  """
  pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
  sorted_students = collection.aggregate(pipeline)

  return sorted_students
