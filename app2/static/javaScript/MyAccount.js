if (sessionStorage.getItem("Access_Token") === null){
    window.location.href="/";
}

// Role Based Change
var role=sessionStorage.getItem("Role");
if (role === 'User'){
    document.getElementById('RoleChange').style.display = 'none';
}

//  sending name to the Dashboard 
$(document).ready(function () {
    const name = sessionStorage.getItem("Username");
    $("#username").text(name);
})


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



//  sending name,email and passsword to the my Account 
$(document).ready(function () {
    const name=sessionStorage.getItem("Username");
    const mail=sessionStorage.getItem("Email");
    const role=sessionStorage.getItem("Role");

    $("#Username").text(name);
    $("#Email").text(mail);
    $("#Role").text(role);
});


// If clicking logout then removing contents on the session storage and moving to the home page
function logout(){
    sessionStorage.removeItem("Access_Token");
    sessionStorage.removeItem("Username");
    sessionStorage.removeItem("Email");
    sessionStorage.removeItem("Role");
}

