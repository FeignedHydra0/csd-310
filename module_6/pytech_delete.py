from pydoc import doc
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

records = [
    {
        "student_id": "1010",
        "first_name": "John",
        "last_name": "Doe"
    }
]

print("-- INSERT STATEMENTS --")
for record in records:
    new_student_Id = pytech.insert_one(record).inserted_id
    new_student_fName = record.get("first_name")
    new_student_lName = record.get("last_name") 
    print("Inserted student record "+str(new_student_fName)+" "+str(new_student_lName)+" into the students collection with document_id "+str(new_student_Id))

cursor = pytech.find(
    {"student_id":"1010"}
    )

print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
for record in cursor:
    print("Student ID: "+record["student_id"])
    print("First Name: "+record["first_name"])
    print("Last Name: "+record["last_name"])
    print("")

deleteRecord = pytech.delete_one({"student_id":"1010"})

cursor = pytech.find()

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for record in cursor:
    print("Student ID: "+record["student_id"])
    print("First Name: "+record["first_name"])
    print("Last Name: "+record["last_name"])
    print("")