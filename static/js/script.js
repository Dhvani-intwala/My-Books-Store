// $(document).ready(function() {
//     // Add a click event listener to the subscribe button
//     $('#subscriber').click(function() {
//         // Change the URL to 'example.com/newsletter'
//         console.log("click")
       

//         // Trigger the modal to open (you might need to use a delay to ensure the URL change happens first)
//         setTimeout(function() {
//             $('#exampleModal').modal('show');
//         }, 100);
//     });
// });
document.addEventListener("DOMContentLoaded", function() {
    // Find the element by ID
    var button = document.getElementById("subscriber");
    var modal = new bootstrap.Modal(document.getElementById("exampleModal"));
    // Check if the element exists
    if (button) {
        // Attach a click event handler
        button.addEventListener("click", function() {
            // Perform your operation here
            // window.location.href = '/newsletter';
            history.pushState({}, null, "/newsletter");
            modal.show();

        });
    }
});