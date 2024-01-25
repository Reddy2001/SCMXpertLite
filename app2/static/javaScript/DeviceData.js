if (sessionStorage.getItem("Access_Token") === null) {
    window.location.href = "/";
} else if (sessionStorage.getItem("Role") === "User") {
    window.location.href = "/deviceDataUser"
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






// getting form data and sending to the server
document.addEventListener("DOMContentLoaded", function () {
    // TOGGLE SIDEBAR --> to display the sidebar after clicking the menu icon 
    const menuBar = document.querySelector('#content nav .bx.bx-menu');
    const sidebar = document.getElementById('sidebar');

    menuBar.addEventListener('click', function () {
        sidebar.classList.toggle('hide');
    })
    document.getElementById("submit").addEventListener("click", function (event) {
        event.preventDefault();
        console.log(sessionStorage.getItem("Access_Token"));
        const token = sessionStorage.getItem("Access_Token");
        const formData = new FormData(document.getElementById("form_data"));
        formData.append("DeviceId", $("#DeviceId").val());
        console.log(formData.get("DeviceId"));
        fetch("/deviceData", {
            method: "POST",
            headers: {
                'Authorization': `Bearer ${token}`
            },
            body: formData
        }).then(response => {
            if (response.status === 200) {

                return response.json();
            }
            console.log(response)

        }).then(response => {
            if (response.status_code === 400) {
                console.log("response", response.detail);
                $("#error").text(response.detail);
            }
            $("#id").text(response[0].Device_Id);
            // console.log("data", response,response[0].Device_Id);
            let DeviceData = "";
            for (let i = 0; i < response.length; i++) {
                const Data = response[i];

                DeviceData = DeviceData + "<tr><td>"
                    + Data.Device_Id + "</td><td>"
                    + Data.Battery_Level + "</td><td>"
                    + Data.First_Sensor_Temperature + "</td><td>"
                    + Data.Route_From + "</td><td>"
                    + Data.Route_To + "</td><td>"
                    + Data.Timestamp + "</td></tr>"
                    
            }
            console.log(DeviceData);
            $("#data").html(DeviceData);
            console.log(data);

        }).catch(error => {
            $("#error").text(error.message);
            $("#error").css("visibility", "visible");

        });

    });
});



// If clicking logout then removing contents on the session storage and moving to the home page
function logout() {
    sessionStorage.removeItem("Access_Token");
    sessionStorage.removeItem("Username");
    sessionStorage.removeItem("Email");
    sessionStorage.removeItem("Role");
}