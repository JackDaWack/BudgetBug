from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware as CORS
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from pymongo import MongoClient
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORS,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

frontend_path = Path(__file__).parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
def home(request: Request):
    incoming_user = request.cookies.get("user")
    if not incoming_user:
        return RedirectResponse(url="/login.html")
    print("We're live!")
    return FileResponse(frontend_path / "index.html")

def signal_recieved():
    print("We made contact!")

@app.post("/api/run")
async def run_function():
    signal_recieved()
    return {"status": "success"}

def database_connect():
    return MongoClient("mongodb://localhost:27017/")["budgetbug_db"]