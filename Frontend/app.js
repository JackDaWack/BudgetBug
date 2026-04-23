//Logout function that sends a POST request to the /logout endpoint, removes the access token from local storage, 
//and redirects the user to the login page.
async function logout() {
    await fetch("/logout", {method: "POST", credentials: "include"});
    localStorage.removeItem("access_token"); 
    window.location.href = "/login-page";
}

async function loadUser() {
    try {
        const res = await fetch("/api/me", {method: "GET", credentials: "include"});
        if (!res.ok) throw new Error();
        const user = await res.json();
        document.getElementById("welcome-message").textContent = `Welcome to BudgetBug, ${user.username}!`;
    } catch {
        window.location.href = "/login-page";
    }
}

async function create_new_budget() {}

async function view_budgets() {}

document.addEventListener("DOMContentLoaded", loadUser);
document.getElementById("logoutBtn").addEventListener("click", logout);
document.getElementById("budget-options").addEventListener("change", async (e) => {
    const contentDiv = document.getElementById("budgets_content");
    contentDiv.innerHTML = "";
    if (e.target.value === "create_new_budget") {
        //await create_new_budget();
        contentDiv.textContent = "Create New Budget functionality coming soon!";
    } else if (e.target.value === "view_budgets") {
        //await view_budgets();
        contentDiv.textContent = "View Budgets functionality coming soon!";
    }
});