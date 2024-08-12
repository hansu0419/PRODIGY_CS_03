function togglePasswordVisibility() {
    var passwordInput = document.getElementById('text');
    var passwordVisibilityToggle = document.getElementById('show-password');
    if (passwordVisibilityToggle.checked) {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
}