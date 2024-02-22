
// TOGGLE SIDEBAR --> to display the sidebar after clicking the menu icon 
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
    sidebar.classList.toggle('hide');
})


// Getting Success Message and Error Message
const successMessage = document.getElementById('success');
const errorMessage = document.getElementById('Error');

// Hiding the Error Message and Success Message
function hideSuccessMessage() {
    successMessage.style.display = 'none';
}
function hideErrorMessage() {
    errorMessage.style.display = 'none';
}

// Delay in milliseconds (e.g., 3000 for 3 seconds)
const delay = 3000;

// Hiding Error and Success messages after Delay time
setTimeout(hideSuccessMessage, delay);
setTimeout(hideErrorMessage, delay);


// Role Based Change for feedback
var role=document.getElementById('role').innerText;
if (role === 'User'){
    document.getElementById('view_user_feedback').style.display = 'none';
}else{
    document.getElementById('feedback').style.display= 'none';
}

