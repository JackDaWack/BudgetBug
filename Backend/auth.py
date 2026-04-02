#import main
import sqlite3
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from email_validator import validate_email, EmailNotValidError
import bcrypt

router = APIRouter()

#app = main.app

class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {"username" : self.username, "email" : self.email, "password" : self.password}

class Login_Data(BaseModel):
    username: str
    password: str

class Register_Data(BaseModel):
    username: str
    email: str
    password: str

def retrieve_user(username: str):
    db = main.database_connect()
    if db["users"].find_one({"username": username}):
        return User(db["users"].find_one({"username": username})["username"], db["users"].find_one({"username": username})["email"], db["users"].find_one({"username": username})["password"])
    return None

def get_user(username: str):
    db = sqlite3.connect("users.db").cursor()
    db.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = db.fetchone()
    db.connection.close()
    if user:
        return {"id": user[0], "username": user[1], "email": user[2], "password": user[3]}
    return None

def create_user(username: str, email: str, password: str):
    db = sqlite3.connect("users.db").cursor()
    db.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    db.connection.commit()
    db.connection.close()

@router.post("/login")
def login(data: Login_Data):
    user = get_user(data.username)
    if user and bcrypt.checkpw(data.password.encode('utf-8'), user["password"]):
        response = JSONResponse(content={"success": True})
        response.set_cookie(key="user", value=data.username)
        return response
    return {"success": False}

@router.post("/register")
def register(data: Register_Data):
    if get_user(data.username):
        return JSONResponse(content={"success": False, "message": "Username already exists"})
    if get_user(data.email):
        return JSONResponse(content={"success": False, "message": "Email already exists"})
    try:
        validate_email(data.email)
    except EmailNotValidError as e:
        return {"success": False, "message": str(e)}
    
    hashed_password = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())
    
    create_user(data.username, data.email, hashed_password)

    response = JSONResponse(content={"success": True, "message": "User registered successfully"})
    
    return JSONResponse(content={"success": True, "message": "User registered successfully"})

@router.post("/logout")
def logout():    
    response = JSONResponse(content={"success": True})
    response.delete_cookie(key="user")
    return response