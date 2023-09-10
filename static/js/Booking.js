$(document).ready(function() {
    $('#bookingForm').on('submit', function(event) {
        event.preventDefault();
        var bookingData = {
            pickup_date: $('#pickup-date').val(),
            pickup_location: $('#pickup-location').val(),
            dropoff_date: $('#dropoff-date').val(),
            dropoff_location: $('#dropoff-location').val(),
            vehicle_type: $('#vehicle').val()
        };
        $.ajax({
            url: '/book-vehicle',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(bookingData),
            success: function(response) {
                console.log(response);
                // You can add code here to handle the response from the server
                if (response.bookingExists) {
                    alert('Booking already exists!');
                } else if (response.bookingSuccess) {
                    alert('inorder to finish booking Please proceed to payment method.');
                    window.location.href = '/payment-methods';
                }
            },
            error: function(error) {
                console.log(error);
                // You can add code here to handle errors
                alert('An error occurred. Please check another booking.');
            }
        });
    });
});
