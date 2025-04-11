# delete_data.py

import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

def delete_all_documents(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]

    # Delete all documents in the collection
    result = collection.delete_many({})
    print(f"{result.deleted_count} documents deleted from '{collection_name}' collection in '{db_name}' database.")

    client.close()

if __name__ == "__main__":
    uri = os.getenv("MONGODB_URI")
    db_name = input("Enter the database name: ")
    collection_name = input("Enter the collection name to delete documents from: ")
    delete_all_documents(uri, db_name, collection_name)
