import main

app = main.app

class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {"username" : self.username, "email" : self.email, "password" : self.password}

def retrieve_user(username: str):
    db = main.database_connect()
    if db["users"].find_one({"username": username}):
        return User(db["users"].find_one({"username": username})["username"], db["users"].find_one({"username": username})["email"], db["users"].find_one({"username": username})["password"])
    return None

@app.get("/login")
def login(username: str, password: str):
    db = main.database_connect()
    if db["users"].find_one({"username": username}):
        if db["users"].find_one({"username": username})["password"] is password:
            return {"status": "success", "message": "User logged in successfully"}
    return {"status": "error", "message": "User login failed."}

@app.get("/register")
def register(username: str, email: str, password: str):
    db = main.database_connect()
    if db["users"].find_one({"username": username}):
        return {"status": "error", "message": "Username already exists"}
    user = User(username, email, password)
    db["users"].insert_one(user.to_dict())
    return {"status": "success", "message": "User registered successfully"}
