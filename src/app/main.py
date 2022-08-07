from fastapi import FastAPI

from app.common.router import router as common_router
from app.core.sqlite.client import sqlite3
from app.nearest_hawkercentre.router import router as nearest_hawkercentre_router

app = FastAPI()

app.include_router(
    common_router, 
    prefix="", 
    tags=["Core"])
app.include_router(
    nearest_hawkercentre_router, 
    prefix="/finder", 
    tags=["Nearest Hawker Centre"])

@app.on_event("shutdown") 
async def app_shutdown():
    # clear up resources on shutdown
    sqlite3.conn.close()