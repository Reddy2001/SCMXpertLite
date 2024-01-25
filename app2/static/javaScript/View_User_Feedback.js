if (sessionStorage.getItem("Access_Token") === null) {
    window.location.href = "/";
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
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
    sidebar.classList.toggle('hide');
})



console.log(sessionStorage.getItem("Username"));
//  sending name to the Dashboard 
document.addEventListener("DOMContentLoaded", function () {
    $(document).ready(function () {
        $("#username").text(sessionStorage.getItem("Username"));
    });
});


// Pushing Feedback Data to the frontend
$(document).ready(function () {
    const token = sessionStorage.getItem("Access_Token");
    fetch(`/viewUserFeedbacks`, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
            'Content-Type': 'application/json',
        },
    })
        .then(response => {
            if (response.status !== 200) {
                throw new Error(`Status ${response.status}`);
            }
            return response.json();
        }).then(response => {
            if (response.status_code === 400) {
                console.log("response", response.detail);
                $("#error").text(response.detail);
            }
            console.log("data",response);
            let Feedback = "";
            for (let i = 0; i < response.length; i++) {
                const Data = response[i];

                Feedback = Feedback + "<tr><td>"
                    + Data.name + "</td><td>"
                    + Data.Email + "</td><td>"
                    + Data.rating + "</td><td>"
                    + Data.opinion + "</td></tr>"
            }
            console.log(Feedback);
            $("#data").html(Feedback);
            console.log(data);
        }).catch(error => {
            // alert(error.message);

        })
});


// If clicking logout then removing contents on the session storage and moving to the home page
function logout() {
    sessionStorage.removeItem("Access_Token");
    sessionStorage.removeItem("Username");
    sessionStorage.removeItem("Email");
    sessionStorage.removeItem("Role");
}