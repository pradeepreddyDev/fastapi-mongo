from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from typing import Optional

from server.database import (
    retrieve_people_counting_donut,
    get_all_devices,
    retrieve_people_counting_graph
)


router = APIRouter()


@router.get("/devices", response_description="People counting donut")
async def get_devices():
    record = await get_all_devices()
    if record:
        return record
    return {}


@router.get("/people-counting-donut", response_description="People counting donut")
async def get_people_counting_donut(serial: Optional[str] = None):
    record = await retrieve_people_counting_donut(serial)
    if record:
        return record
    return {}


@router.get("/people-counting-graph", response_description="People counting graph")
async def get_people_counting_graph(serial: Optional[str] = None):
    record = await retrieve_people_counting_graph(serial)
    if record:
        return record
    return {}
