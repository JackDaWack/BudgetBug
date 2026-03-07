import main

app = main.app

class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
    
    def to_dict(self):        
        return {"username": self.username,"email": self.email,"password": self.password}

def retrieve_user(username: str):
    db = main.database_connect()
    user_data = db.users.find_one({"username": username})
    if user_data:
        return User(user_data["username"], user_data["email"], user_data["password"])
    return None

@app.get("/login")
def login():
    return

@app.get("/register")
def register():
    return

