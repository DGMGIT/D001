from datetime import datetime
import pytz as pytz
from fastapi import FastAPI

# a simple demonstration of the get

app = FastAPI()


@app.get("/hello/world")
async def root():
    return {"message": "Hello World"}


@app.get("/zone/time")
async def fetch_time(city, country):
    location = country + '/' + city
    zone = pytz.timezone(location)
    dt = datetime.now(zone)
    return dt.strftime("%Z") + dt.strftime("%c")
