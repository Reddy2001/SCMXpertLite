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


// // Send the getAccess_token to the FastAPI backend
// const getJwtToken = () => {
//     const token = localStorage.getItem('access_token');
//     return token;
// };


// // Accessing and using the JWT token
// const jwtToken = getJwtToken();

// if (jwtToken) {
//     console.log('JWT Token:', jwtToken);

//     // Fetch data from a signin FastAPI endpoint
//     fetch('http://127.0.0.1:8000/myShipment', {
//         method: 'GET',
//         headers: {
//             'Authorization': `Bearer ${jwtToken}`,
//             'Content-Type': 'application/json',
//         },
//     })
// } else {
//     console.log("TOken is not present")
// }


// // Method to delete the access token on local storage
// function signOut(){
//     localStorage.clear("access_token");
// }