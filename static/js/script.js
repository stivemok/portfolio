$(document).ready(function() {
    $('.login100-form').submit(function(event) {
        event.preventDefault();
        var email = $('input[name="email"]').val();
        var password = $('input[name="pass"]').val();
        $.ajax({
            url: '/login',
            data: {
                email: email,
                password: password
            },
            type: 'POST',
            success: function(response) {
                if (response == 'success') {
                    showPopup();
                    window.location.href = '/admin';
                } else {
                    alert('Invalid user name or password');
                }
            }
        });
    });
});

function showPopup() {
    swal({
        title: 'Login successful',
        icon: 'success',
        timer: 70000,
        buttons: false
    });
}