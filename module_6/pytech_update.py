import collections
from pydoc import doc
from unittest import result
from xml.etree.ElementPath import find
from pymongo import InsertOne, MongoClient


from pymongo import MongoClient
import pymongo.mongo_client

url = "mongodb+srv://admin:admin@cluster0.w5mlyq8.mongodb.net/?retryWrites=true&w=majority";

client = MongoClient(url);
db = client.pytech

pytech = db["students"]

cursor = pytech.find()

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for record in cursor:
    print("Student ID: "+record["student_id"])
    print("First Name: "+record["first_name"])
    print("Last Name: "+record["last_name"])
    print("")
    result = pytech.update_one(
        {"student_id":"1007"},
        {
            "$set":{
                "last_name":"Blackbeard"
            }
        }
    )

cursor = pytech.find(
    {"student_id":"1007"}
    )

print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
for record in cursor:
    print("Student ID: "+record["student_id"])
    print("First Name: "+record["first_name"])
    print("Last Name: "+record["last_name"])
    print("")