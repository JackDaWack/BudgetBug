async function login(username, password) {}

async function register(username, email, password) {}

const login_button = document.getElementById("login-button");
const register_button = document.getElementById("register-button");

login_button.addEventListener("click",login());
register_button.addEventListener("click",register());