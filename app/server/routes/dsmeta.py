from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from typing import Optional

from server.database import (
    retrieve_people_counting_donut,
    get_all_devices,
    retrieve_people_counting_graph,
    retrieve_alert,
    retrieve_path_tracing,
    retrieve_rush_hour_prediction
)

from server.helpers.datetime_helper import generate_start_end_day_unix_string, generate_start_end_day_unix_string_rush_hour


router = APIRouter()


@router.get("/devices", response_description="People counting donut")
async def get_devices():
    record = await get_all_devices()
    if record:
        return record
    return {}


@router.get("/people-counting-donut", response_description="People counting donut")
async def get_people_counting_donut(serial: Optional[str] = None, date: Optional[str] = None):
    record = await retrieve_people_counting_donut(serial, generate_start_end_day_unix_string(date))
    if record:
        return record
    return {}


@router.get("/people-counting-graph", response_description="People counting graph")
async def get_people_counting_graph(serial: Optional[str] = None, date: Optional[str] = None):
    record = await retrieve_people_counting_graph(serial, generate_start_end_day_unix_string(date))
    if record:
        return record
    return {}


@router.get("/alerts", response_description="Alerts")
async def get_dashboard_alerts(serial: Optional[str] = None, date: Optional[str] = None):
    record = await retrieve_alert(serial, generate_start_end_day_unix_string(date))
    if record:
        return record
    return {}


@router.get("/path-tracing", response_description="Path Tracing in dashboard")
async def get_dashboard_path_tracing(serial: Optional[str] = None, date: Optional[str] = None):
    record = await retrieve_path_tracing(serial, generate_start_end_day_unix_string(date))
    if record:
        return record
    return {}


@router.get("/rush-hour-prediction", response_description="Rush hour prediction")
async def get_rush_hour_prediction_fetch_hourly_basis(serial: Optional[str] = None, date: Optional[str] = None):
    record = await retrieve_rush_hour_prediction(serial, generate_start_end_day_unix_string_rush_hour(date))
    if record:
        return record
    return {}
