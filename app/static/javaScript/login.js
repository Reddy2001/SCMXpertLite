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



// Getting Error Message
const errorMessage = document.getElementById('error');

// Hiding the Error Message
function hideErrorMessage() {
    errorMessage.style.display = 'none';
}

// Delay in milliseconds (e.g., 3000 for 3 seconds)
const delay = 3000;

// Hiding Error message after Delay time
setTimeout(hideErrorMessage, delay);


function Verify_Captcha(){
  const captcha = localStorage.getItem("_grecaptcha")
  console.log(captcha,"captcha")
  if(captcha == "")
  {
    window.alert("Please Verify Captcha..")
    window.location.href='/signin'
  }
}

// if (grecaptcha.getResponse() == ""){
//   alert("You can't proceed!");
// } else {
//   alert("Thank you");
// }