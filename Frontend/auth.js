console.log("auth.js loaded");

//Login function that sends a POST request to the /login endpoint with the username and password, 
//and redirects to the main page if successful. This is linked in the login.html file as a form submission handler.
async function login() {
    try {
        const username = document.querySelector("#login-form #username").value;
        const password = document.querySelector("#login-form #password").value;
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

//Registration function that sends a POST request to the /register endpoint with the username, email, and password, 
//and redirects to the login page if successful. This is linked in the register.html file as a form submission handler.
async function register() {
    try {
        const username = document.querySelector("#register-form #username").value;
        const email = document.querySelector("#register-form #email").value;
        const password = document.querySelector("#register-form #password").value;
        const response = await fetch("/register", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({username,email,password})})
        const data = await response.json();
        console.log("Server response:", data);
        if (data.success) {
            window.location.href = "/login-page";
        } else {
            alert(data.message || "Registration failed");
        }
    }
    catch(err){console.error("Error calling backend:", err);}

}

document.addEventListener("DOMContentLoaded", function() {
    const login_form = document.getElementById("login-form");
    const register_form = document.getElementById("register-form");
    
    if (login_form) {
        login_form.addEventListener("submit", async (e) => {e.preventDefault(); await login();});
    }
    if (register_form) {
        register_form.addEventListener("submit", async (e) => {e.preventDefault(); await register();});
    }
});