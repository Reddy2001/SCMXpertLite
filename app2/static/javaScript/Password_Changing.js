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


document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("submit").addEventListener("click", function (event) {
        event.preventDefault();
        console.log(sessionStorage.getItem("Access_Token"));
        const token = sessionStorage.getItem("Access_Token");
        const formData = new FormData(document.getElementById("form_data"));
        formData.append("Old_Password", $("#old_pw").val());
        formData.append("New_Password", $("#new_pw").val());
        formData.append("Re_type_Password", $("#conform_pw").val());
        console.log(formData.get("Old_Password"), formData.get("New_Password"), formData.get("Re_type_Password"));
        fetch("/passwordChanging", {
            method: "POST",
            headers: {
                'Authorization': `Bearer ${token}`
            },
            body: formData
        }).then(response => {
            if (response.status === 200) {
                console.log(response);
                // window.location.href='myAccount';
                return response.json();
            }
            else {
                // If the status code is not 200, handle the error
                return response.json().then(errorData => {
                    // Log and display the error message
                    console.log(errorData.Error);
                    $("#error").text(errorData.Error);
                    // Throw an error 
                    throw new Error(errorData.Error);
                });
            }
        }).then(data => {
            // Process the successful response data

            // Log the data
            console.log(data);

            // Display a success message
            $("#message").text(data.message);
            setTimeout(function () {
                $("#message").text(""); // Clear the  message
            }, 3000)
        }).catch(error => {
            console.log(error.message);
            $("#error").text(error.message);
            // Display the error message for 3 seconds
            setTimeout(function () {
                $("#error").text(""); // Clear the error message
            }, 3000);
        });
    });
});



// sending name to the Password Changing page
console.log(sessionStorage.getItem("Username"));
$(document).ready(function () {
    const name = sessionStorage.getItem("Username");
    $("#user").text(name);
})




// If clicking logout then removing contents on the session storage and moving to the home page
function logout() {
    sessionStorage.removeItem("Access_Token");
    sessionStorage.removeItem("Username");
    sessionStorage.removeItem("Email");
    sessionStorage.removeItem("Role");
}

