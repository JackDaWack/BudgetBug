async function login() {
    try {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        const response = await fetch("/login", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({username,password})})
        if (!response.ok) {
            throw new Error("Login request failed");
        }

        const data = await response.json();
        console.log("Server response:", data);
    }
    catch(err){console.error("Error calling backend:", err);}

}

async function register(username, email, password) {
    try{
        const response = await fetch("/register", {method: "POST"})

    }
    catch(err){console.error("Error calling backend:", err);}
}

const login_button = document.getElementById("login-button");
const register_button = document.getElementById("register-button");

login_button.addEventListener("click",login());
register_button.addEventListener("click",register());