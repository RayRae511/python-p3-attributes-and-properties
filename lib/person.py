#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
     def __init__(self):
        self._name = None
        
     def name(self):
         self._name.title()
         return self._name
    
     def name(self, val):
        if (val, str) and 1 <= len(val) <= 25:
            self._name = val
        else:
            print("Name must be string between 1 and 25 characters")
     def job(self):
        return self._job
     def job(self, val):
        if val in APPROVED_JOBS:
            self._job = val
        else:
            print("Job must be in list of approved jobs")

name = Person()
name.name = "Ray"
name.job = "Gaming"
#Output: "Job must be in list of approved jobs"