document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll('.btn.btn-primary');
    buttons.forEach(function(button) {
        button.disabled = true; // Change 'True' to 'true' in JavaScript
    });
}); 
document.addEventListener("DOMContentLoaded", function() {
    const backButton = document.getElementById('goBack');
    backButton.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default anchor behavior
        history.back();  // Go to the previous page in history
    });
});

