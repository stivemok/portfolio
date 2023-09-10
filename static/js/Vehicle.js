$(document).ready(function() {
    $('.btn').on('click', function(event) {
        event.preventDefault();

        // Redirect to booking page
        window.location.href = "/booking";
    });
});

let currentImageIndex = 0;

function changeSlide(direction) {
  currentImageIndex += direction;
  $.ajax({
    url: '/get-images',
    type: 'POST',
    data: { index: currentImageIndex },
    success: function(response) {
      $('.slide1').attr('src', response.imageSrc1);
      $('.slide2').attr('src', response.imageSrc2);
      updateDescription(currentImageIndex);
    }
  });
}

function updateDescription(index) {
  $.ajax({
    url: '/get-vehicle-info',
    type: 'POST',
    data: { index: index },
    success: function(response) {
      $('.make').text(`Make: ${response.make}`);
      $('.model').text(`Model: ${response.model}`);
      $('.year').text(`Year: ${response.year}`);
      $('.condition').text(`Condition: ${response.condition}`);
      $('.color').text(`Color: ${response.color}`);
      $('.price').text(`Price: ${response.price}`);
    }
  });
}

function updateSlideAndDescription(direction) {
  changeSlide(direction);
}
