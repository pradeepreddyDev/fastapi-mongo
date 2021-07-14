import motor.motor_asyncio
from bson.objectid import ObjectId
from pymongo import DESCENDING
import pymongo
from .helpers.db_dashboard import *
import time
from bson import SON


MONGO_DETAILS = "mongodb://192.168.0.104:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

db = client["starbucks"]
col = db["dsmeta"]


async def retrieve_people_counting_donut(serial):
    record = await col.find_one({'serial': serial}, sort=[('_id', pymongo.DESCENDING)])
    if record:
        return dsmeta_people_counting_donut_helper(record)


async def retrieve_people_counting_graph(serial):
    records = []
    async for record in col.find({'serial': serial}):
        records.append(people_counting_graph_helper(record))
    return records


async def get_all_devices():
    response = await db.command(SON([("distinct", "dsmeta"), ("key", "serial")]))
    if response:
        return response['values']
    return {}
