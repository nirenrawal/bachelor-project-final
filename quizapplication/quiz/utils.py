import os
from pymongo import MongoClient 
from dotenv import load_dotenv

load_dotenv()

def get_database_handle():
    client = MongoClient(
        host=os.environ.get('MONGO_HOST'), 
        port=int(os.environ.get('MONGO_PORT')), 
        username=os.environ.get('MONGO_NAME'), 
        password=os.environ.get('MONGO_PASSWORD')
    )

    database_handle = client[os.environ.get('MONGO_DATABASE')]

    return database_handle, client