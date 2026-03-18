from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware as CORS
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from pymongo import MongoClient
from pathlib import Path
from auth import router as auth_router

app = FastAPI()
app.include_router(auth_router)


app.add_middleware(
    CORS,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

frontend_path = Path(__file__).parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

def database_connect():
    return MongoClient("mongodb://localhost:27017/")["budgetbug_db"]

@app.get("/login-page")
def login_page():
    return FileResponse(frontend_path / "login.html")

@app.get("/register-page")
def register_page():
    return FileResponse(frontend_path / "register.html")

@app.get("/")
def home(request: Request):
    #db = database_connect()
    #if db["users"].find_one({"username": "Developer01"}):
    #    print("Developer01 exists in the database")
    incoming_user = request.cookies.get("user")
    if not incoming_user:
        return RedirectResponse(url="/login-page")
    print("We're live!")
    return FileResponse(frontend_path / "index.html")

def signal_recieved():
    print("We made contact!")

@app.post("/api/run")
async def run_function():
    signal_recieved()
    return {"status": "success"}

