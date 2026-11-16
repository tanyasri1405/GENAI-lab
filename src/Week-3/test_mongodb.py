
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")

try:
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    print("MongoDB connected successfully!")

    db = client["llm_monitoring"]
    collection = db["api_usage"]

    print("Database:", db.name)
    print("Collection:", collection.name)

    client.close()

except Exception as error:
    print("MongoDB connection failed:")
    print(error)
