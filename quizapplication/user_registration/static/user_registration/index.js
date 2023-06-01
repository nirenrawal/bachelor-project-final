
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


//--------------- Handle error message on create question ---------------------//

// function handleFormSubmit(){
//     const form = document.getElementById('question-form');
//     form.addEventListener('submit', async (e) => {
//         e.preventDefault();
//         try {
//             const response = await fetch('add_quiz_question/', {
//                 method: 'POST',
//                 body: new FormData(form)
//             });
//             if (response.ok) {
//                 window.location.href = 'add_quiz_question/';
//             } else {
//                 const errorData = await response.json();
//                 const errorMessage = errorData.error_Message;
//                 const errorElement = document.getElementById('error-msg');
//                 errorElement.textContent = errorMessage;
//                 errorElement.style.display = 'block';
//                 setTimeout(() => {
//                     errorElement.style.display = 'none';
//                 }, 2000)
//             }
//         } catch (error) {
//                 console.log('Error', error)
//             }
//     });
// }

// handleFormSubmit()



