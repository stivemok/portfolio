	const vehicleTypeSelect = document.getElementById('vehicle-type');
        const sedanImage = document.getElementById('sedan-image');
        const compactImage = document.getElementById('compact-image');
        const suvImage = document.getElementById('suv-image');
        const truckImage = document.getElementById('truck-image');
        const vanImage = document.getElementById('van-image');

        vehicleTypeSelect.addEventListener('change', () => {
            const selectedVehicle = vehicleTypeSelect.value;
            // Hide all vehicle images
            sedanImage.style.display = 'none';
            compactImage.style.display = 'none';
            suvImage.style.display = 'none';
            truckImage.style.display = 'none';
            vanImage.style.display = 'none';

            // Show the selected vehicle image container
            if (selectedVehicle === 'sedan') {
                sedanImage.style.display = 'block';
            } else if (selectedVehicle === 'compact') {
                compactImage.style.display = 'block';
            } else if (selectedVehicle === 'suv') {
                suvImage.style.display = 'block';
            } else if (selectedVehicle === 'truck') {
                truckImage.style.display = 'block';
            } else if (selectedVehicle === 'van') {
                vanImage.style.display = 'block';
            }
        });
	 //
        var selectElement = document.getElementById("vehicle-type");
        var displayElement = document.getElementById("sedan-image");

        let slideIndex = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(n) {
    if (n >= slides.length) {
        slideIndex = 0;
    } else if (n < 0) {
        slideIndex = slides.length - 1;
    }

    slides.forEach(slide => slide.style.display = 'none');
    slides[slideIndex].style.display = 'block';
}

function changeSlide(n) {
    slideIndex += n;
    showSlide(slideIndex);
}

showSlide(slideIndex);
