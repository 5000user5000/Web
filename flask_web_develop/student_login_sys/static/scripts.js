/* Handle the password visibility toggle */
function togglePassword() {
    const passwordInput = document.getElementById('password');
    const passwordToggle = document.getElementById('password-toggle');
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        passwordToggle.classList.replace('fa-eye', 'fa-eye-slash');
    } else {
        passwordInput.type = 'password';
        passwordToggle.classList.replace('fa-eye-slash', 'fa-eye');
    }
}

  /* Attach the password visibility toggle to the toggle button */
    const passwordToggle = document.getElementById('password-toggle');
    passwordToggle.addEventListener('click', togglePassword);
