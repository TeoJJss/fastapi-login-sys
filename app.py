from fastapi import FastAPI, Request, APIRouter
from services.service import *
import os
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

if not os.path.isfile(auth_db):
    create_db()

@router.post("/ticket")
async def create_ticket(request: Request):
    # Get request body
    body = await request.json()
    name=body['name']
    password=body['password']

    # Generate ticket
    ticket = generate_ticket(name, password)
    if ticket == None: # Invalid user
        return JSONResponse(content={"msg": "Unauthenticated"}, status_code=401)

    # Insert ticket to DB
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

@router.delete("/logout")
def delete(ticket:str):
    delete_ticket(ticket)
    return JSONResponse({"msg": "Delete ticket success"}, status_code=200)

app.include_router(router, prefix="/api")