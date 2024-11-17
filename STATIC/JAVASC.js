// TRIGGER UPLOAD
const uploadIcon = document.getElementById('upload-icon');
const fileInput = document.getElementById('file');
const imgArea = document.querySelector('.img-area');
const clearButton = document.querySelector('.clear-image');
const identifyButton = document.querySelector('.select-image'); // Identify button
const nextButton = document.querySelector('.next-button');

// Initially disable the identify button
identifyButton.disabled = true;

if (nextButton) {
    nextButton.style.display = 'none';
}

// When the upload icon is clicked, trigger the file input
uploadIcon.addEventListener('click', () => {
    fileInput.click();  // This will open the file picker dialog
});

// SHOW PIC
fileInput.addEventListener('change', function () {
    const image = this.files[0];
    if (image && image.size < 2000000) { // Ensure the image is under 2MB
        const reader = new FileReader();
        reader.onload = () => {
            // Remove any previous images
            const allImg = imgArea.querySelectorAll('img');
            allImg.forEach(item => item.remove());
            
            // Create an image element and set its source
            const img = document.createElement('img');
            img.src = reader.result;
            img.classList.add('uploaded-image'); // Add a class to style if needed

            // Append the image to the image area
            imgArea.appendChild(img);
            imgArea.classList.add('active');  // Add 'active' class for visibility
            imgArea.dataset.img = image.name; // Store the file name (optional)
            
            // Enable the identify button once a valid image is uploaded
            identifyButton.disabled = false;
        }
        reader.readAsDataURL(image);  // Convert image to data URL
    } else {
        alert("Image size exceeds 2MB");
        identifyButton.disabled = true;  // Keep the button disabled if image is invalid
    }
});

// Clear the image when the "Clear" button is clicked
clearButton.addEventListener('click', () => {
    const allImg = imgArea.querySelectorAll('img');
    allImg.forEach(item => item.remove()); // Remove all images in the imgArea
    imgArea.classList.remove('active'); // Remove 'active' class
    imgArea.dataset.img = ''; // Clear the stored image data
    fileInput.value = ''; // Reset the file input so a new image can be uploaded

    // Disable the identify button when image is cleared
    identifyButton.disabled = true;
    if (nextButton) nextButton.style.display = 'none';
});

// HANDLE PREDICTION RESPONSE
function handlePredictionResponse(prediction) {
    if (prediction) {
        if (nextButton) {
            nextButton.style.display = 'inline-block'; // Show next button if prediction is available
            nextButton.disabled = false;
        }
    } else {
        if (nextButton) {
            nextButton.style.display = 'none'; // Hide next button if no prediction
            nextButton.disabled = true;
        }
    }
}

// Loading screen handling
window.onload = function() {
    setTimeout(function(){
        const loadingScreen = document.getElementById('loading-screen');
        const pageContent = document.querySelector('.page-content');
        
        if (loadingScreen) {
            loadingScreen.style.display = 'none'; // Hide loading screen
        }
        if (pageContent) {
            pageContent.style.display = 'block'; // Show main content
        }
    }, 3000); // Adjust the duration for loading screen as needed
};
