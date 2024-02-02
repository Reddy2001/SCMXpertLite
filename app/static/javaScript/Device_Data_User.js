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


// On Loading this page the error messages will display one by one based on the delay time
document.addEventListener("DOMContentLoaded", function () {
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



$(document).mousemove(function (event) {
    $('.torch').css({
      'top': event.pageY,
      'left': event.pageX
    });
  });