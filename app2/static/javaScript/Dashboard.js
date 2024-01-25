if (sessionStorage.getItem("Access_Token") === null) {
    window.location.href="/";
}



// Code for displaying active links
const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item => {
    const li = item.parentElement;

    item.addEventListener('click', function () {
        allSideMenu.forEach(i => {
            i.parentElement.classList.remove('active');
        })
        li.classList.add('active');
    })
});




// TOGGLE SIDEBAR --> to display the sidebar after clicking the menu icon 
document.addEventListener("DOMContentLoaded", function () {
    const menuBar = document.querySelector('#content nav .bx.bx-menu');
    const sidebar = document.getElementById('sidebar');

    menuBar.addEventListener('click', function () {
        sidebar.classList.toggle('hide');
    });

    // Role Based Change for feed back
    var role = sessionStorage.getItem("Role");
    if (role === 'User') {

        document.getElementById('view_user_feedback').style.display = 'none';
    } else if (role === "Admin") {
        document.getElementById('feedback').style.display = 'none';
    }

});



// // Getting Success Message
// const successMessage = document.getElementById('success');

// // Hiding the Error Message
// function hideSuccessMessage() {
//     successMessage.style.display = 'none';
// }

// // Delay in milliseconds (e.g., 3000 for 3 seconds)
// const delay = 3000;

// // Hiding Error message after Delay time
// setTimeout(hideSuccessMessage, delay);

console.log(sessionStorage.getItem("Username"));
//  sending name to the Dashboard 
document.addEventListener("DOMContentLoaded", function () {
    $(document).ready(function () {
        $("#user").text(sessionStorage.getItem("Username"));
    });
});


// If clicking logout then removing contents on the session storage and moving to the home page
function logout() {
    sessionStorage.removeItem("Access_Token");
    sessionStorage.removeItem("Username");
    sessionStorage.removeItem("Email");
    sessionStorage.removeItem("Role");
}