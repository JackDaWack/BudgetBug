#import main
import sqlite3
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from email_validator import validate_email, EmailNotValidError
import bcrypt

router = APIRouter()

#Data models for login and registration requests.
class Login_Data(BaseModel):
    username: str
    password: str

class Register_Data(BaseModel):
    username: str
    email: str
    password: str

#Helper functions for database interactions, including getting a user by username, creating a new user, and validating email addresses.
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

#The login endpoint checks the provided credentials against the database and sets a cookie if successful.
@router.post("/login")
def login(data: Login_Data):
    user = get_user(data.username)
    if user and bcrypt.checkpw(data.password.encode('utf-8'), user["password"]):
        response = JSONResponse(content={"success": True})
        response.set_cookie(key="user", value=data.username)
        return response
    return {"success": False}

#The registration endpoint checks for existing users and validates the email before creating a new user.
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
    create_user(data.username, data.email, bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt()))
    return JSONResponse(content={"success": True, "message": "User registered successfully"})


