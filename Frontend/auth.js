async function login(username, password) {
    try {
        const response = await fetch("/login", {method: "POST"})
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