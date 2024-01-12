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



                 // For data validations

// Get the current date 
function getCurrentDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = (today.getMonth() + 1).toString().padStart(2, '0');
    const day = today.getDate().toString().padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// Set the minimum date for the date input field
document.getElementById("DeliveryDate").min = getCurrentDate();




                // For setting delay time for the error messages

// Getting Error Message
const errorMessage = document.getElementById('error');
const successMessage = document.getElementById('success');

// Hiding the Error Message
function hideErrorMessage() {
    errorMessage.style.display = 'none';
}

// Hiding the success Message
function hideSuccessMessage() {
    successMessage.style.display = 'none';
}

// Delay in milliseconds (e.g., 3000 for 3 seconds)
const delay = 3000;

// Hiding Error message and Success message after Delay time
setTimeout(hideErrorMessage, delay);
setTimeout(hideSuccessMessage, delay);







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
//     fetch('http://127.0.0.1:8000/newShipment', {
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