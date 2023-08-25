$('#bookingForm').submit(function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get the form data
    let formData = $(this).serialize();

    // Send an AJAX request to the Flask server
    $.ajax({
        type: 'POST',
        url: '/search-vehicle',
        data: formData,
        success: function(response) {
            // Create a new HTML page to display the response
            let newWindow = window.open();
            newWindow.document.write(response);
            newWindow.document.close();
        }
    });
});

