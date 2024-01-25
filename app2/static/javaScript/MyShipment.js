if (sessionStorage.getItem("Access_Token") === null) {
    window.location.href="/";
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



// Pushing Shipment Data to the frontend
$(document).ready(function () {
    const token = sessionStorage.getItem("Access_Token");
    fetch(`/myShipmentData`, {
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
            let Shipment = "";
            for (let i = 0; i < response.length; i++) {
                const shipment = response[i];

                Shipment = Shipment + "<tr><td>"
                    + shipment.ShipmentNumber + "</td><td>"
                    + shipment.ContainerNumber + "</td><td>"
                    + shipment.RouteDetails + "</td><td>"
                    + shipment.GoodsType + "</td><td>"
                    + shipment.DeviceName + "</td><td>"
                    + shipment.DeliveryDate + "</td><td>"
                    + shipment.PO_Number + "</td><td>"
                    + shipment.DeliveryNumber + "</td><td>"
                    + shipment.NDC_Number + "</td><td>"
                    + shipment.BatchId + "</td><td>"
                    + shipment.SerialNumber + "</td></tr>"
            }
            console.log(Shipment);
            $("#data").html(Shipment);
            console.log(data);
        }).catch(error => {
            // alert(error.message);

        })
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