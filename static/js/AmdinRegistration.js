document.querySelector('.register100-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var email = document.querySelector('#email').value;
    var pass = document.querySelector('#pass').value;
    var confirmPass = document.querySelector('#confirm-pass').value;
    if (pass !== confirmPass) {
        alert('Password and Confirm Password must be identical!');
    } else {
        $.ajax({
            type: 'POST',
            url: '/register',
            data: { email: email, pass: pass, 'confirm-pass': confirmPass },
            success: function(response) {
                if (response === 'Email already taken!') {
                    alert('The email you entered is already taken. Please try again with a different email.');
                } else if (response.url) {
                    // If the server responds with a URL, redirect to that URL
                    window.location.href = response.url;
                } else {
                    alert(response);
                }
            }
        });
    }
});
