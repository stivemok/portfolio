document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();
        let fname = document.querySelector('#fname').value;
        let mname = document.querySelector('#mname').value;
        let lname = document.querySelector('#lname').value;
        let phone = document.querySelector('#phone').value;
        let email = document.querySelector('#email').value;
        let vehicle = document.querySelector('#vehicle').value;
        let year = document.querySelector('#year').value;

        // Get the values of the new form fields for ID/Passport and Car Registration
        let idpassport = document.querySelector('#idpassport').files[0];
        let carreg = document.querySelector('#carreg').files[0];

        // Create a new window object
        let newWindow = window.open();

        // Write the form submission results to the new window as a new HTML document
        newWindow.document.write("<!DOCTYPE html>");
        newWindow.document.write("<html>");
        newWindow.document.write("<head>");
        newWindow.document.write("    <title>Registered sucessfuly</title>");
        newWindow.document.write("</head>");
        newWindow.document.write("<body>");
        newWindow.document.write("    <h1>Registered sucessfuly</h1>");
        newWindow.document.write(`    <p>First Name: ${fname}</p>`);
        newWindow.document.write(`    <p>Middle Name: ${mname}</p>`);
        newWindow.document.write(`    <p>Last Name: ${lname}</p>`);
        newWindow.document.write(`    <p>Phone Number: ${phone}</p>`);
        newWindow.document.write(`    <p>Email Address: ${email}</p>`);
        newWindow.document.write(`    <p>Vehicle Type: ${vehicle}</p>`);
        newWindow.document.write(`    <p>Release Year: ${year}</p>`);

        // Write the values of the new form fields for ID/Passport and Car Registration to the new window
        if (idpassport) {
            newWindow.document.write(`    <p>ID/Passport: ${idpassport.name}</p>`);
        } else {
            newWindow.document.write("    <p>ID/Passport: Not provided</p>");
        }
        
        if (carreg) {
            newWindow.document.write(`    <p>Car Registration: ${carreg.name}</p>`);
        } else {
            newWindow.document.write("    <p>Car Registration: Not provided</p>");
        }

        newWindow.document.write("</body>");
        newWindow.document.write("</html>");
    });
});
