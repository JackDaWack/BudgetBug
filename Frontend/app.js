//Logout function that sends a POST request to the /logout endpoint, removes the access token from local storage, 
//and redirects the user to the login page.
async function logout() {
    await fetch("/logout", {method: "POST", credentials: "include"});
    localStorage.removeItem("access_token"); 
    window.location.href = "/login-page";
}

const logoutBtn = document.getElementById("logoutBtn");
if (logoutBtn) {
    logoutBtn.addEventListener("click", logout);
}
