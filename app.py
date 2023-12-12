from fastapi import FastAPI, Request, APIRouter
from services.service import *
import sqlite3, os
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from config import AUTH_DB

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

auth_db=AUTH_DB

@router.post("/ticket")
async def create_ticket(request: Request):
    
    ticket = generate_ticket()
    body = await request.json()
    name=body['name']
    password=body['password']

    if not os.path.isfile(auth_db):
        create_db()
    insert_ticket(ticket, name)

    return JSONResponse(content={"ticket": ticket}, status_code=201)

@router.get("/auth")
def auth(ticket:str):
    name_ls=get_name(ticket)
    if len(name_ls) != 1:
        return JSONResponse({"msg": "Invalid user"}, status_code=401)
    else:
        name=name_ls[0][0]
    return JSONResponse({"username": name}, status_code=200)

app.include_router(router, prefix="/api")