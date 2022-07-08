from pymongo import MongoClient
import pymongo.mongo_client

url = "mongodb+srv://admin:admin@cluster0.w5mlyq8.mongodb.net/?retryWrites=true&w=majority";

client = MongoClient(url);
db = client.pytech
print(db.list_collection_names)
