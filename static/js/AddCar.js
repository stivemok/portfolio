document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();
        let make = document.querySelector('#make').value;
        let model = document.querySelector('#model').value;
        let year = document.querySelector('#year').value;
        let condition = document.querySelector('#condition').value;
        let color = document.querySelector('#color').value;
        let price = document.querySelector('#price').value;
	let PlateNo = document.querySelector('#PlateNo').value;
        let vehicle = document.querySelector('#vehicle').value;
	// Get the values of the new form fields for Car Photo 1 and Car Photo 2
        let photo1 = document.querySelector('#photo1').files[0];
        let photo2 = document.querySelector('#photo2').files[0];

        // Create a FormData object to hold the form data
        let formData = new FormData();
        formData.append('make', make);
        formData.append('model', model);
        formData.append('year', year);
        formData.append('condition', condition);
        formData.append('color', color);
        formData.append('price', price);
	formData.append('PlateNo', PlateNo);
	formData.append('vehicle', vehicle);
        // Append the values of the new form fields for Car Photo 1 and Car Photo 2 to the FormData object
        if (photo1) {
            formData.append('photo1', photo1, photo1.name);
        }

        if (photo2) {
            formData.append('photo2', photo2, photo2.name);
        }
	 // Send an AJAX request to the server-side script
        $.ajax({
            type: 'POST',
            url: '/submit_car',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
              // Handle the response from the server-side script
                  if (response === 'success') {
                    alert(response);
                   } else {
                    alert(response);
                   }
            }
        });
    });
});
