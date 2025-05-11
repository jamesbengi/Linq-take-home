from pymongo import MongoClient

def setup_mongo_client():  
    """
    Set up a MongoDB client and return the database and collection.
    """
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    
    # Create or connect to a database
    db = client["linq_database"]
    
    # Create or connect to a collection
    collection = db["linq_take_home"]
    
    return client, db, collection
client, db, collection = setup_mongo_client()
