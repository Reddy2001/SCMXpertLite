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


// Role Based Change for feed back
var role=document.getElementById('role').innerText;
if (role === 'User'){

    document.getElementById('view_user_feedback').style.display = 'none';
}else if(role ==="Admin"){
    document.getElementById('feedback').style.display= 'none';
}


// Getting Success Message
const successMessage = document.getElementById('success');

// Hiding the Error Message
function hideSuccessMessage() {
    successMessage.style.display = 'none';
}

// Delay in milliseconds (e.g., 3000 for 3 seconds)
const delay = 3000;

// Hiding Error message after Delay time
setTimeout(hideSuccessMessage, delay);





// // Getting access_token from Dashboard.html
// var token = document.getElementById("access_token").innerText

// //Storing access_token to the local storage
// localStorage.setItem("access_token", token);

// // Getting access_token from Local Storage
// var getAccess_token = localStorage.getItem("access_token")




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
//     fetch('http://127.0.0.1:8000/token', {
//         method: 'GET',
//         headers: {
//             'Authorization': `Bearer ${jwtToken}`,
//             'Content-Type': 'application/json',
//         },
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Handle the response data
//         console.log(data);
//     })
//     .catch(error => {
//         console.error('Error fetching data:', error);
//     });
// } else {
//     console.log("TOken is not present")
// }



// // Method to delete the access token on LOcal Storage
// function signOut(){
//     localStorage.clear("access_token");
// }