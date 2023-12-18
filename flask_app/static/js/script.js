function displaySelectedImage(event, elementId) {
    const selectedImage = document.getElementById(elementId);
    const fileInput = event.target;

    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();

        reader.onload = function(e) {
            selectedImage.src = e.target.result;
        };

        reader.readAsDataURL(fileInput.files[0]);
    }
}

function myChangeFunction(event, image_file) {
    var imagePath = document.getElementById('image_path');
    console.log(image_file.value);
    text = image_file.value.replace("C:\\fakepath\\", '');
    console.log(text);
    imagePath.value = text;
    console.log(imagePath.value);
}

function displayForm() {
    var inputs = document.getElementById("inputContainer");
    inputs.className = "row";
}