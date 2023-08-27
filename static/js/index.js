// Wait for the document to be ready
document.addEventListener("DOMContentLoaded", function () {
    // Get a reference to the form element
    var bookingForm = document.getElementById("bookingForm");

    // Add an event listener for form submission
    bookingForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission

        // Serialize the form data
        var formData = new FormData(bookingForm);

        // Construct the URL for the search results page
        var searchResultsURL = "/search-results?" + new URLSearchParams(formData);

        // Open the search results in a new tab
        window.open(searchResultsURL, "_blank");
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

      // 
