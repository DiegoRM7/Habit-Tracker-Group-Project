// functions to display images and change value of inputs that will go to DB as the image_filename
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

// shows form when button clicked
function displayForm(inputContainerForHabitName) {
    var inputs = document.getElementById(inputContainerForHabitName);
    inputs.className = "row fade-in-text justify-content-center";
}
// on update page: trying to delete other forms around it when one is shown or to move the side forms to the middle if possible
function centerTheSideForms(sideForm) {
    var movableForm = document.querySelector(sideForm)
    movableForm.style.left = "50%";
    movableForm.style.top = "50%";
    document.getElementById("my-element").remove();
}

// to show a password reset button and popup
function resetPasswordPopUp() {
    let text;
    let person = prompt("Please verify your email address:",);
    if (person == null || person == "") {
        text = "User cancelled password reset.";
    } else {
        text = "An email has been sent to " + person + "if it exists in the database";
    }
    document.getElementById("demo").innerHTML = text;
    document.getElementById("demo").style = "color: red";
}