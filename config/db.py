from pymongo import MongoClient
MONGO_URI="mongodb+srv://ammalkhaalil_db_user:nevertrust14$A@cluster0.j9k2wqi.mongodb.net/"
conn=MongoClient(MONGO_URI)

db = conn["notes"]            # database name
notes = db["notes"]  