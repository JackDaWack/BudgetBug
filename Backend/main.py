from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    print("We're live!")
    return {"message": "We're live!"}