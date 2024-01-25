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







// On Loading this page the error messages will display one by one based on the delay time
document.addEventListener("DOMContentLoaded", function () {
    // TOGGLE SIDEBAR --> to display the sidebar after clicking the menu icon 
    const menuBar = document.querySelector('#content nav .bx.bx-menu');
    const sidebar = document.getElementById('sidebar');

    menuBar.addEventListener('click', function () {
        sidebar.classList.toggle('hide');
    })
    setTimeout(function () {
        document.querySelector('.heading').style.display = 'block';
    }, 250);

    setTimeout(function () {
        document.querySelector('.content').style.display = 'block';
    }, 750);

    setTimeout(function () {
        document.querySelector('.redirect').style.display = 'block';
    }, 1250);
});


// If clicking logout then removing contents on the session storage and moving to the home page
function logout() {
    sessionStorage.removeItem("Access_Token");
    sessionStorage.removeItem("Username");
    sessionStorage.removeItem("Email");
    sessionStorage.removeItem("Role");
}
