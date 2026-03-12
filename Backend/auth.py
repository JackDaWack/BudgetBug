import main
from pydantic import BaseModel

app = main.app

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

@app.post("/login")
def login(data: Login_Data):
    db = main.database_connect()
    user = db["users"].find_one({"username": data.username})
    if user and user["password"] == data.password:
        return {"status": "success", "message": "User logged in successfully"}
    return {"status": "error", "message": "User login failed"}

@app.post("/register")
def register(data: Register_Data):
    db = main.database_connect()
    if db["users"].find_one({"username": data.username}):
        return {"status": "error", "message": "User already exists"}
    user  = User(data.username,data.email,data.password)
    db["users"].insert_one(user.to_dict())
    return {"status": "success", "message": "User registered in successfully"}