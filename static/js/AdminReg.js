document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.login100-form').addEventListener('submit', function(event) {
        event.preventDefault();
        let email = document.querySelector('input[name="email"]').value;
        let password = document.querySelector('input[name="pass"]').value;
        let confirmPassword = document.querySelectorAll('input[name="pass"]')[1].value;

        if (password === confirmPassword) {
            // Display the success message using an alert
            alert(`Registered successfully with email: ${email}`);
        } else {
            // Display an error message on the page when the passwords do not match
            let message = 'Error: Passwords do not match';
            let messageElement = document.createElement('p');
            messageElement.textContent = message;
            document.querySelector('.container-login100').appendChild(messageElement);
        }
    });
});