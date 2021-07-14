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
        # "serial": record["serial"]
    }
