from fastapi import FastAPI
from supabase import create_client, Client

from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI()

default_table_name = "item"
t_name = str(None)


# a simple demonstration of the function currently supported by the supebase.py and way to use them
# E.G. get and post doesn't included signup/in


# get all row in item table
@app.get('/item/all')
async def get_all():
    data = supabase.table(default_table_name).select("*").execute()
    assert len(data.get("data", [])) > 0
    return data


# set selected table by user input name
@app.get('/item/set/name/')
async def set_table_name(table_name):
    global t_name
    t_name = table_name
    data = supabase.table(t_name).select("*").execute()
    assert len(data.get("data", [])) > 0
    return data


# get all row in selected table
@app.get('item/all/name')
async def get_table():
    data = supabase.table(t_name).select("*").execute()
    assert len(data.get("data", [])) > 0
    return data


# get selected item in item table based on id number
@app.get('/item/get/id')
async def get_select(item_id):
    # get all items in selected table
    # data = supabase.table("item").select('*').eq('id', item_id).execute()
    # get id & name of items in selected table
    data = supabase.table("item").select('id, id', 'name, name').eq('id', item_id).execute()
    assert len(data.get("data", [])) > 0
    return data


# get selected item in item table based on user input id number and table name
@app.get('/item/get/name/id')
async def get_select_name(item, item_id):
    # get id & name of items in selected table
    data = supabase.table(item).select('id, id', 'name, name').eq('id', item_id).execute()
    assert len(data.get("data", [])) > 0
    return data


# creates new table
@app.post('/item/create')
async def create_table(item_id, name):
    data = supabase.table(default_table_name).insert(
        {'id': item_id, 'name': name, 'created_at': str(datetime.utcnow())}).execute()
    # assert if insert response is a success
    assert data.get("status_code") in (200, 201)
    return data
