from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware as CORS
from pymongo import MongoClient

app = FastAPI()

app.add_middleware(
    CORS,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    print("We're live!")
    return {"message": "We're live!"}

def signal_recieved():
    print("We made contact!")

@app.post("/api/run")
async def run_function():
    signal_recieved()
    return {"status": "success"}

def database_connect():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    return db