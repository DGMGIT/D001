from fastapi import FastAPI
from supabase import create_client, Client

import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI()

# a simple demonstration of the signup/in function currently supported by the supebase.py


@app.post('/sign/up/test')
async def sign_up():
    user = supabase.auth.sign_up(
        email='example@email.com',
        password='example-password',
    )


@app.get('/sign/in/test')
async def sign_in():
    user = supabase.auth.sign_in(
        email='example@email.com',
        password='example-password'
    )


@app.post('/sign/up')
async def sign_up(email, password):
    user = supabase.auth.sign_up(
        email=email,
        password=password,
    )


@app.get('/sign/in')
async def sign_in():
    user = supabase.auth.sign_in(
        email='example@email.com',
        password='example-password'
    )