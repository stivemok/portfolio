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
        let PlateNo = document.querySelector('#PlateNo').value;
        let make = document.querySelector('#make').value;
        let model = document.querySelector('#model').value;
        let color = document.querySelector('#color').value;
        let price = document.querySelector('#price').value;
        let condition = document.querySelector('#condition').value;
        // Get the values of the new form fields for ID/Passport and Car Registration
        let idpassport = document.querySelector('#idpassport').files[0];
        let carreg = document.querySelector('#carreg').files[0];

        // Get the values of the new form fields for Car Photo 1 and Car Photo 2
        let photo1 = document.querySelector('#photo1').files[0];
        let photo2 = document.querySelector('#photo2').files[0];

        // Create a FormData object to hold the form data
        let formData = new FormData();
        formData.append('fname', fname);
        formData.append('mname', mname);
        formData.append('lname', lname);
        formData.append('phone', phone);
        formData.append('email', email);
        formData.append('vehicle', vehicle);
        formData.append('year', year);
	formData.append('PlateNo', PlateNo);
        formData.append('make', make);
        formData.append('model', model);
        formData.append('color', color);
        formData.append('price', price);
        formData.append('condition', condition);
        // Append the values of the new form fields for ID/Passport and Car Registration to the FormData object
        if (idpassport) {
            formData.append('idpassport', idpassport, idpassport.name);

        }
        
        if (carreg) {
            formData.append('carreg', carreg, carreg.name);
        }

	// Append the values of the new form fields for Car Photo 1 and Car Photo 2 to the FormData object
	if (photo1) {
	    formData.append('photo1', photo1, photo1.name);
	}
	
	if (photo2) {
	    formData.append('photo2', photo2, photo2.name);
	}

	// Create a new Date object to get the current date and time
	let currentDate = new Date();

	
	// Append the current date and time to the FormData object
	 formData.append('submissionDate', currentDate);

        // Send an AJAX request to the server-side script
        $.ajax({
            type: 'POST',
            url: '/submit-form',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                // Handle the response from the server-side script
                if (response === 'success') {
                    alert("Registered successfully!");
                } else {
                    alert(response);
                }
            }
        });
    });
});
