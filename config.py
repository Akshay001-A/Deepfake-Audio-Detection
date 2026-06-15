from pymongo import MongoClient

MONGO_URI = "mongodb+srv://akshay02072005_db_user:Akshay07123123@deepfake.pmyxjrv.mongodb.net/?appName=Deepfake"

client = MongoClient(MONGO_URI)

db = client["deepfake_db"]

users_collection = db["users"]