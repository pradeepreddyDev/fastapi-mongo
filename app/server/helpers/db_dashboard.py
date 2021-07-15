from csv import DictWriter
from datetime import date
import os


def dsmeta_people_counting_donut_helper(record) -> dict:
    return {
        "serial": record["serial"],
        "ts": record["ts"],
        "num_mask": record["num_mask"],
        "num_no_mask": record["num_no_mask"],
        "entry": record["entry"],
        "exit": record["exit"],
    }


def people_counting_graph_helper(record) -> dict:
    return {
        "ts": record["ts"],
        "count": int(record["entry"]) + int(record["exit"]),
    }


def alert_helper(record) -> dict:
    return {
        "serial": record["serial"],
        "ts": record["ts"],
        "label": record["label"],
        "image": record["image"]
    }


def path_tracing_helper(record) -> dict:
    return {
        "serial": record["serial"],
        "ts": record["ts"],
        "objects": record["objects"],
    }


def rush_hour_helper(record) -> dict:
    try:
        dict = {
            "datetime": record["ts"],
            "count": int(record["entry"]) + int(record["exit"]),
        }

        field_names = ['datetime', 'count']
        with open(f'app/server/CSV/{str(date.today())}.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(dict)
            f_object.close()
        return True
    except Exception as e:
        print(e)
        return False
