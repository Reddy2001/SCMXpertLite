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



 // JavaScript for generating random alphanumeric captcha
 function generateCaptcha() {
  var txt = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
  var captcha = '';
  for (var i = 0; i < 6; i++) {
    captcha += txt.charAt(Math.floor(Math.random() * txt.length));
  }
  return captcha;
}

document.getElementById('refresh').addEventListener('click', function() {
  var cap =  generateCaptcha();
  $('#captcha').text(cap);
  document.getElementById('original_captcha').value=cap;
  console.log(cap);
});

// Initial captcha generation
// document.getElementById('captcha').textContent = generateCaptcha();
var txt = generateCaptcha();
$('#captcha').text(txt);
// $("#original_captcha").text(txt);
document.getElementById('original_captcha').value=txt;
console.log(document.getElementById('original_captcha').innerText);




// Getting Error Message and success message
const errorMessage = document.getElementById('error');
const SuccessMessage = document.getElementById('msg')

// Hiding the Error Message and success message
function hideErrorMessage() {
  errorMessage.style.display = 'none';
}
function hideSuccessMessage() {
  SuccessMessage.style.display = 'none';
}

// Delay in milliseconds (e.g., 3000 for 3 seconds)
const delay = 3000;

// Hiding Error message after Delay time
setTimeout(hideErrorMessage, delay);
setTimeout(hideSuccessMessage, delay);

