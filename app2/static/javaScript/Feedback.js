// Function to get the JWT token from sessionStorage
function getJwtToken() {
  return sessionStorage.getItem("Access_Token");
}

const feedbackForm = document.getElementById('feedbackForm');
document.addEventListener("DOMContentLoaded", function () {

  const allStar = document.querySelectorAll('.rating .star')
  const ratingValue = document.querySelector('.rating input')

  allStar.forEach((item, idx) => {
    item.addEventListener('click', function () {
      let click = 0
      ratingValue.value = idx + 1

      allStar.forEach(i => {
        i.classList.replace('bxs-star', 'bx-star')
        i.classList.remove('active')
      })
      for (let i = 0; i < allStar.length; i++) {
        if (i <= idx) {
          allStar[i].classList.replace('bx-star', 'bxs-star')
          allStar[i].classList.add('active')
        } else {
          allStar[i].style.setProperty('--i', click)
          click++
        }
      }
      console.log(click, ratingValue.value, allStar)
    })
  })
  console.log("rating", ratingValue.value);
  feedbackForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const yourJwtToken = sessionStorage.getItem("Access_Token");
    console.log(yourJwtToken);
    const rating = ratingValue.value;
    const formData = new FormData(document.getElementById("feedbackForm"));
    formData.append("rating", rating); // Corrected line
    formData.append("opinion", $("#opinion").val());
    console.log(formData.get("opinion"), formData.get("rating")); // Corrected line
    fetch("/feedback", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${yourJwtToken}`
      },
      body: formData
    })
      .then(response => {
        console.log(response);
        if (response.status !== 200) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      }).then(data => {
        console.log("Response data:", data.message);
        // Display a success message
        $("#message").text(data.message);
        setTimeout(function () {
          $("#message").text(""); // Clear the  message
        }, 3000)
        window.alert("Thanks for your Feedback")
        window.location.href = "/dashboard"

      })
      .catch(error => {
        console.error("Error:", error);
      });
  });
});
