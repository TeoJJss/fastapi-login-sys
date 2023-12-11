from fastapi import FastAPI, status
from services.service import *
import sqlite3, os

app=FastAPI()

@app.post("/ticket/{name}", status_code=status.HTTP_201_CREATED)
def create_ticket(name):
    
    ticket = generate_ticket()

    if not os.path.isfile("auth.db"):
        create_db()
    insert_ticket(ticket, name)

    return {"ticket": ticket}