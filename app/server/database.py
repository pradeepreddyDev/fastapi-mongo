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
alerts_col = db["dsalerts"]


async def retrieve_people_counting_donut(serial, start_end_unix):
    record = await col.find_one({'ts': {'$lt': start_end_unix['etunix'], '$gt': start_end_unix['stunix']}, 'serial': serial},  sort=[('_id', pymongo.DESCENDING)])
    if record:
        return dsmeta_people_counting_donut_helper(record)


async def retrieve_people_counting_graph(serial, start_end_unix):
    records = []
    async for record in col.find({'ts': {'$lt': start_end_unix['etunix'], '$gt': start_end_unix['stunix']}, 'serial': serial}):
        records.append(people_counting_graph_helper(record))
    return records


async def get_all_devices():
    response = await db.command(SON([("distinct", "dsmeta"), ("key", "serial")]))
    if response:
        return response['values']
    return {}


async def retrieve_alert(serial, start_end_unix):
    record = await alerts_col.find_one({'ts': {'$lt': start_end_unix['etunix'], '$gt': start_end_unix['stunix']}, 'serial': serial},  sort=[('_id', pymongo.DESCENDING)])
    if record:
        return alert_helper(record)
    return {}


async def retrieve_path_tracing(serial, start_end_unix):
    record = await col.find_one({'ts': {'$lt': start_end_unix['etunix'], '$gt': start_end_unix['stunix']}, 'serial': serial},  sort=[('_id', pymongo.DESCENDING)])
    if record:
        return path_tracing_helper(record)
    return {}


async def retrieve_rush_hour_prediction(serial, start_end_unix):
    if os.path.exists(f'app/server/CSV/{str(date.today())}.csv'):
        os.remove(f'app/server/CSV/{str(date.today())}.csv')
    try:
        async for record in col.find({'ts': {'$lt': start_end_unix['etunix'], '$gt': start_end_unix['stunix']}, 'serial': serial}):
            rush_hour_helper(record)
        return {"hour": "3PM", "avg_walkins": "30", "max_wakins": "50"}
    except Exception as e:
        print(str(e))
        return {}
