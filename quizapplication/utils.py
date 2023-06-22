from pymongo import MongoClient
import environ
env = environ.Env()
environ.Env.read_env()

def get_db_handle():

    client = MongoClient(
        host=env("MONGO_HOST"), 
        port=int(env("MONGO_PORT")), 
        username=env("MONGO_USER"), 
        password=env("MONGO_PASSWORD")
    )

    db_handle = client[env("MONGO_DB_NAME")]
    return db_handle, client