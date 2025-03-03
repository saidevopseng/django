function showLogin() {
    document.getElementById("signup-form").classList.remove("active");
    document.getElementById("login-form").classList.add("active");
}

function showSignup() {
    document.getElementById("login-form").classList.remove("active");
    document.getElementById("signup-form").classList.add("active");
}

// Set login form as the default view
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("login-form").classList.add("active");
});
