from pydoc import doc
from xml.etree.ElementPath import find
from pymongo import InsertOne, MongoClient


from pymongo import MongoClient
import pymongo.mongo_client

url = "mongodb+srv://admin:admin@cluster0.w5mlyq8.mongodb.net/?retryWrites=true&w=majority";

client = MongoClient(url);
db = client.pytech

pytech = db["students"]

docs = pytech.find()

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() Query --")

for doc in docs:
    print("Student ID: "+doc["student_id"])
    print("First Name: "+doc["first_name"])
    print("Last Name: "+doc["last_name"])

findRecord = pytech.find_one({"student_id": "1008"})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() Query --")

for record in findRecord:
    print("Student ID: "+findRecord["student_id"])
    print("First Name: "+findRecord["first_name"])
    print("Last Name: "+findRecord["last_name"])