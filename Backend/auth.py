#import main
import sqlite3
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from fastapi import APIRouter
from email_validator import validate_email, EmailNotValidError

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
    #db = main.database_connect()
    #user = db["users"].find_one({"username": data.username})
    #if user and user["password"] == data.password:
    #    return {"status": "success", "message": "User logged in successfully"}
    #return {"status": "error", "message": "User login failed"}
    if get_user(data.username) and get_user(data.username)["password"] == data.password:
        return RedirectResponse(url="/", status_code=302)
    return {"status": "error", "message": "User login failed"}

@router.post("/register")
def register(data: Register_Data):
    #db = main.database_connect()
    #if db["users"].find_one({"username": data.username}):
    #    return {"status": "error", "message": "User already exists"}
    #user = User(data.username, data.email, data.password)
    #db["users"].insert_one(user.to_dict())
    #return {"status": "success", "message": "User registered in successfully"}
    if data.username and data.email and data.password:
        try:
            validate_email(data.email)
        except EmailNotValidError as e:
            return {"status": "error", "message": str(e)}
    create_user(data.username, data.email, data.password)
    return RedirectResponse(url="/login-page", status_code=302)