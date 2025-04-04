document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let rememberMe = document.getElementById('rememberMe').checked;

    if (email === "" || password === "") {
        alert("Please fill in all fields.");
        return;
    }

    // Simulating authentication (Replace with actual backend call)
    if (email === "admin@example.com" && password === "password123") {
        alert("Login successful!");
        if (rememberMe) {
            localStorage.setItem("rememberedEmail", email);
        }
        window.location.href = "dashboard.html"; // Redirect to dashboard
    } else {
        alert("Invalid email or password.");
    }
});

// Auto-fill email if remembered
window.onload = function() {
    let rememberedEmail = localStorage.getItem("rememberedEmail");
    if (rememberedEmail) {
        document.getElementById('email').value = rememberedEmail;
    }
};

// Toggle password visibility
document.getElementById("togglePassword").addEventListener("click", function() {
    let passwordInput = document.getElementById("password");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        this.classList.replace("fa-eye", "fa-eye-slash");
    } else {
        passwordInput.type = "password";
        this.classList.replace("fa-eye-slash", "fa-eye");
    }
});
