
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



//--------------- Error Alert ---------------------//

