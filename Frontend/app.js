async function detect_signal() {
    console.log("Signal Detected!");
    try {
        const response = await fetch("/api/run", {method: "POST"});
        const data = await response.json();
        console.log("Backend response:", data);
    } catch (err) {
        console.error("Error calling backend:", err);
    }

}
async function logout() {
    try {
        const response = await fetch("/logout", {method: "POST"});
        const data = await response.json();
        console.log("Backend response:", data); 
        if (data.success) {
            window.location.href = "/login-page";
        } else {
            alert("Logout failed");
        } 
    } catch (err) {
        console.error("Error calling backend:", err);
    }
}


const signal = document.getElementById("signal");
signal.addEventListener("click", detect_signal);

const logOutButton = document.getElementById("log-out-button");
logOutButton.addEventListener("click", logout);