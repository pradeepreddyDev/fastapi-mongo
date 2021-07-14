
import pymongo


client = pymongo.MongoClient("mongodb://192.168.0.104:27017")

# Database Name
db = client["starbucks"]

# Collection Name
col = db["dsmeta"]

x = col.find_one()

print(x)
