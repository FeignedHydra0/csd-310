from pydoc import doc
from xml.etree.ElementPath import find
from pymongo import InsertOne, MongoClient


from pymongo import MongoClient
import pymongo.mongo_client

url = "mongodb+srv://admin:admin@cluster0.w5mlyq8.mongodb.net/?retryWrites=true&w=majority";

client = MongoClient(url);
db = client.pytech

pytech = db["students"]

records = [
    {
        "student_id": "1007",
        "first_name": "Jake",
        "last_name": "Wilson"
    },
    {
        "student_id": "1008",
        "first_name": "Johhny",
        "last_name": "Marley"
    },
    {
        "student_id": "1009",
        "first_name": "Jill",
        "last_name": "Barnet"
    }
]

print("-- INSERT STATEMENTS --")
for record in records:
    new_student_Id = pytech.insert_one(record).inserted_id
    new_student_fName = record.get("first_name")
    new_student_lName = record.get("last_name") 
    print("Inserted student record "+str(new_student_fName)+" "+str(new_student_lName)+"into the students collection with document_id "+str(new_student_Id))

