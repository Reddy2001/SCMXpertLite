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




// getting form data and sending to the server
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("submit").addEventListener("click", function (event) {
        event.preventDefault();
        console.log(sessionStorage.getItem("Access_Token"));
        const token = sessionStorage.getItem("Access_Token");
        fetch("/newShipment", {
            method: "POST",
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                "Shipment_Number": $("#Shipment_Num").val(),
                "Container_Number": $("#Container_Num").val(),
                "Route_Details": $("#RouteDetails").val(),
                "Goods_Type": $("#Goods").val(),
                "Device": $("#Device").val(),
                "Expected_Delivery": $("#DeliveryDate").val(),
                "PO_Number": $("#POno").val(),
                "Delivery_Number": $("#DeliveryNumber").val(),
                "NDC_Number": $("#NDCNumber").val(),
                "Batch_ID": $("#BatchId").val(),
                "Serial_Number": $("#SerialNumber").val(),
                "Shipment_Description": $("#ShipmentDescription").val(),
            })
        })
            .then(response => {
                if (response.status === 200) {

                    return response.json();
                }
                else {
                    // If the status code is not 200, handle the error
                    return response.json().then(errorText => {
                        console.log("1",errorText.Error); 
                        throw new Error(errorText.Error);
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
                console.log("2",error.message);
                $("#error").text(error.message);
                // Display the error message for 3 seconds
                setTimeout(function () {
                    $("#error").text(""); // Clear the error message
                }, 3000);
            });
    });

});


console.log(sessionStorage.getItem("Username"));
//  sending name to the Dashboard 
document.addEventListener("DOMContentLoaded", function () {
    $(document).ready(function () {
        $("#user").text(sessionStorage.getItem("Username"));
    });
});

// If clicking logout then removing contents on the session storage and moving to the home page
function logout() {
    sessionStorage.removeItem("Access_Token");
    sessionStorage.removeItem("Username");
    sessionStorage.removeItem("Email");
    sessionStorage.removeItem("Role");
}