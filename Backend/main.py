from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

@app.get("/")
def home():
    print("We're live!")
    return {"message": "We're live!"}

def database_connect():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    return db