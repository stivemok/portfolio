 // Add an event listener to the form submission
 document.getElementById("bookingForm").addEventListener("submit", function(event) {
    // Get the selected values
    const pickupDate = document.getElementById("pickup").value;
    const pickupLocation = document.getElementById("pickupLocation").value;
    const dropoffDate = document.getElementById("dropoff").value;
    const dropoffLocation = document.getElementById("dropoffLocation").value;
    const vehicleType = document.getElementById("vehicleType").value;

    // Validate input
    if (!pickupDate || !pickupLocation || !dropoffDate || !dropoffLocation || !vehicleType) {
        alert("Please fill in all fields before submitting.");
        event.preventDefault(); // Prevent the form submission
        return;
    }

    // Construct the query string
    const queryString = `?pickupDate=${pickupDate}&pickupLocation=${pickupLocation}&dropoffDate=${dropoffDate}&dropoffLocation=${dropoffLocation}&vehicle=${vehicleType}`;

    // Redirect to vehicles.html with query parameters
    window.location.href = `vehicles.html${queryString}`;

    event.preventDefault(); // Prevent the default form submission
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

      // 