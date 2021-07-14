from fastapi import FastAPI
from server.routes.dsmeta import router as DsmetaRouter

app = FastAPI()

app.include_router(DsmetaRouter, tags=["DSMetaData"], prefix="/dsmeta")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
