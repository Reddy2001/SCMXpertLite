//This function is used to display Password after clicking on eye icon and also used to hide the password
function togglePassword() {
  var passwordInput = document.getElementById('password');

  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    document.getElementById("eye").className = "far fa-eye";
    document.getElementById("eye").style.color = "blue";

  } else {
    passwordInput.type = 'password';
    document.getElementById("eye").className = "far fa-eye-slash";
    document.getElementById("eye").style.color = "#f1a20f";
  }
}




// Storing JWT token in session storage
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("submit").addEventListener("click", function (event) {
    event.preventDefault();
    const formData = new FormData(document.getElementById("signin-form"));
    formData.append("username", $("#username").val());
    formData.append("password", $("#password").val());
    console.log(formData.get("password"), formData.get("username"));
    fetch("/signin", {
      method: "POST",
      body: formData
    }).then(response => {
      if (response.status === 200) {
        console.log(response);
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
    }).then(response => {
      sessionStorage.setItem("Access_Token", `${response.access_token}`);
      sessionStorage.setItem("Username", `${response.username}`)
      sessionStorage.setItem("Email", `${response.email}`)
      sessionStorage.setItem("Role", `${response.role}`)
      if (sessionStorage.getItem("Access_Token") !== null) {
        window.location.href = "/dashboard";
      }
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



