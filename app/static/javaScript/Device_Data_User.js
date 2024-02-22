
// TOGGLE SIDEBAR --> to display the sidebar after clicking the menu icon 
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
    sidebar.classList.toggle('hide');
})


// On Loading this page the error messages will display one by one based on the delay time
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        document.querySelector('.heading').style.display = 'block';
    }, 250); 
    
    setTimeout(function () {
        document.querySelector('.content').style.display = 'block';
    }, 1000); 
    
    setTimeout(function () {
        document.querySelector('.redirect').style.display = 'block';
    }, 2000); 
});

