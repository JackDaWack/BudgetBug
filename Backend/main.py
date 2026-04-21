from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware as CORS
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from pymongo import MongoClient
from pathlib import Path
import auth
import sqlite3

app = FastAPI()
app.include_router(auth.router)


app.add_middleware(
    CORS,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

frontend_path = Path(__file__).parent.parent / "Frontend"
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

def database_connect():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["budget_app"]
    return db

def init_db():
    db = sqlite3.connect("users.db").cursor()
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password BINARY
        )
    """)
    db.connection.commit()
    db.connection.close()

#Login page endpoint, serves the login.html file to the frontend when the user navigates to /login-page, 
#which is the default page when the user first visits the site.
@app.get("/login-page")
def login_page():
    return FileResponse(frontend_path / "login.html")

#Register page endpoint, serves the register.html file to the frontend when the user navigates to /register-page, 
#which is linked in the login.html file. 
@app.get("/register-page")
def register_page():
    return FileResponse(frontend_path / "register.html")

#Logout endpoint, deletes the user cookie and returns a success message for the frontend to handle 
#and redirect the user to the login page. This is linked in the index.html file as a logout button.
@app.post("/logout")
def logout():
    return JSONResponse(content={"success": True}).delete_cookie(key="user")

#Index page, checks for cookie and redirects to login if not found, otherwise serves index.html
@app.get("/")
def home(request: Request):
    init_db()
    incoming_user = request.cookies.get("user")
    if not incoming_user:
        return RedirectResponse(url="/login-page")
    print("We're live!")
    return FileResponse(frontend_path / "dashboard.html")

@app.get("/create_budget")
def create_budget():
    return FileResponse(frontend_path / "add_income.html")

