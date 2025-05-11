# Data Ingestion into MongoDB

This document explains how data is generated and ingested into a MongoDB collection using Python.

## File Overview

The Python script performs the following tasks:

1. Sets up a MongoDB client using a helper function.
2. Generates random data items.
3. Inserts the data into a MongoDB collection.

---

## MongoDB Setup

```python
from data_store_setup import setup_mongo_client

client, db, collection = setup_mongo_client()
```

`setup_mongo_client()` returns the MongoDB client, the database, and the collection where the data will be stored.

---

## Data Generation

The `generate_data(num_items)` function creates a list of dictionaries with randomized fields:

- `category`: Randomly chosen from a predefined list of Linq product types.
- `value`: A floating-point number between 12 and 60.
- `timestamp`: A datetime object representing a random time.

## Data Insertion

The `insert_data(data)` function inserts the generated data into MongoDB using `insert_many`.
