let currentImageIndex = 0;

// Initialize the slider with the first image and description
        changeSlide(0);

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

