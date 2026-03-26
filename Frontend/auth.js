console.log("auth.js loaded");

const login_button = document.getElementById("login-button");
const login_form = document.getElementById("login-form");
const register_button = document.getElementById("register-button");
const register_form = document.getElementById("register-form");

async function login() {
    try {
        const username = login_form.querySelector("#username").value;
        const password = login_form.querySelector("#password").value;
        const response = await fetch("/login", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({username,password})})
        if (!response.ok) {
            throw new Error("User login request failed");
        }
        const data = await response.json();
        console.log("Server response:", data);
        if (data.success) {
            window.location.href = "/";
        } else {
            alert("Login failed");
        }
    }
    catch(err){console.error("Error calling backend:", err);}

}

async function register() {
    try{
        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        const response = await fetch("/register", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({username,email,password})})
        if (!response.ok) {
            throw new Error("User registry request failed");
        }
        const data = await response.json();
        console.log("Server response:", data);
        if (data.status === "success") {
            window.location.href = "/login-page";
        } else {
            alert(data.message);
        }
    }
    catch(err){console.error("Error calling backend:", err);}
}



login_form.addEventListener("submit", async (e) => {e.preventDefault(); await login();});
if (register_form) {
    register_form.addEventListener("submit", async (e) => {e.preventDefault(); await register();});
}