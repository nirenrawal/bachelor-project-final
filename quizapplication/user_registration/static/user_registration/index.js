
//--------------- Dark Bright Theme ---------------------//

const sun = document.getElementById("sun-icon")
const moon = document.getElementById("moon-icon")
const body = document.getElementsByTagName("body")[0]
const introText = document.querySelector("#intro p")
function darkMode(){
    sun.style.display = "none"
    moon.style.display = "block"
    body.classList.toggle("body-dark")
    introText.style.color="#EEEFF1"
}

function lightMode(){
    sun.style.display = "block"
    moon.style.display = "none"
    body.classList.toggle("body-dark")
    introText.style.color="#3c404a"
}

// ----------- Success & Error Alerts -------

window.addEventListener('load', function() {
    const errorMessage = document.getElementById('success-alert');
    if (errorMessage.innerHTML.trim() !== "") {
        errorMessage.style.display = "block";
        setTimeout(function() {
            errorMessage.style.display = "none";
        }, 2000);
    }
});

window.addEventListener('load', function() {
    const errorMessage = document.getElementById('error-alert');
    if (errorMessage.innerHTML.trim() !== "") {
        errorMessage.style.display = "block";
        setTimeout(function() {
            errorMessage.style.display = "none";
        }, 2000);
    }
});

