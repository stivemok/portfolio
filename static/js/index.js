$(document).ready(function() {
    $('#bookingForm').submit(function(event) {
        event.preventDefault();
        var pickupDate = $('#pickup-date').val();
        var pickupLocation = $('#pickup-location').val();
        var dropoffDate = $('#dropoff-date').val();
        var dropoffLocation = $('#dropoff-location').val();
        var vehicleType = $('#vehicle').val();
        $.ajax({
            url: '/search-vehicle',
            data: JSON.stringify({
                pickup_date: pickupDate,
                pickup_location: pickupLocation,
                dropoff_date: dropoffDate,
                dropoff_location: dropoffLocation,
                vehicle_type: vehicleType
            }),
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            success: function(response) {
                // handle successful response
                if (response === 'Booking already exists check the vehicle page') {
                    alert(response);
                } else {
                    window.location.href = '/vehicles';
                }
            },
            error: function(error) {
                // handle error
                alert('An error occurred while searching for a vehicle. Please try again later.');
            }
        });
    });
});


// carousel function
const carousel = document.querySelector('.carousel');
      const slides = carousel.querySelector('.slides');
      const images = slides.querySelectorAll('img');
      let currentIndex = 0;

      function showSlide(index) {
          slides.style.transform = `translateX(-${index * 100}%)`;
      }

      function nextSlide() {
          currentIndex = (currentIndex + 1) % images.length;
          showSlide(currentIndex);
      }

      setInterval(nextSlide, 3000); // Auto-advance every 3 seconds


