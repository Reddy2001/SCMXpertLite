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
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
    sidebar.classList.toggle('hide');
})




// Role Based Change
var role=document.getElementById('id').innerText;
if (role !== 'Super Admin'){
    document.getElementById('RoleChange').style.display = 'none';
}




// Getting error Message
const successMessage = document.getElementById('error');

// Hiding the Error Message
function hideSuccessMessage() {
    successMessage.style.display = 'none';
}

// Delay in milliseconds (e.g., 3000 for 3 seconds)
const delay = 3000;

// Hiding Error message after Delay time
setTimeout(hideSuccessMessage, delay);

