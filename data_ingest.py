from datetime import datetime, timedelta
from data_store_setup import setup_mongo_client
import random

client,db, collection = setup_mongo_client()
def generate_data(num_items):
    """"
    generate random data for the database
    """
    data=[]
    categories = ["Linq Card Custom", "Linq Card", "Linq Card Metal", "Linq Hub", "Linq MiniCard","Linq Badge"]
    base_time = datetime.now()
    for i in range(num_items):
        days= random.randint(1, 30)
        minutes= random.randint(1, 59)
        timestamp = base_time - timedelta(days=days, minutes=minutes)
        item ={
            "category": random.choice(categories),
            "value": round(random.uniform(12, 60), 2),
            "timestamp": timestamp
        }
        data.append(item)
    return data


def insert_data(data):
    """
    Insert data into the MongoDB collection.
    """
    try:
        collection.insert_many(data)
    except Exception as e:
        print(f"An error occurred: {e}")
sample_data = generate_data(1000)
insert_data(sample_data)