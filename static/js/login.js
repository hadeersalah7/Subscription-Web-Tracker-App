const button = document.querySelector("#submitBtn");
const loginError = document.querySelector("#loginError");
const nameInput = document.querySelector("#name");

// function to set a new entry in the local storage with 'name'
const saveNameToStorage = (name) => {
    // get all the names if it exists in the local storage or return an empty array
    const names = JSON.parse(localStorage.getItem("names") || "[]")
    // if there's a new name push it to the new array:
    names.push(name)

  // set a new key in the localstorage with names and receive the new name array as a string
  localStorage.setItem("names", JSON.stringify(names));

};

button.addEventListener("click", function (event) {
  console.log('test')
    // to validate if the user tries to login without entering his name
    event.preventDefault()
  if (nameInput.value?.trim() == "") {
    loginError.innerHTML = `<p style="color: #b71105; margin-top: 20px">You Can't Login Without Entering Your Name!</p>`;
return;
    // if the name is less than 3 letters then this message shall be displayed
  } else if (nameInput.value?.trim().length < 3) {
    loginError.innerHTML = `<p style="color: #b71105; margin-top: 20px">Name Can't Be Less Than 3 Letters!</p>`;
 return;
    // if the name begin with white or have space
  } else if (/\s/.test(nameInput.value?.trim())) {
    loginError.innerHTML = `<p style="color: #b71105; margin-top: 20px">Name Can't Begin With/Or Have White Spaces!</p>`;
return;
    // if the  name has a number
  } else if (/\d/.test(nameInput.value?.trim())) {
    loginError.innerHTML = `<p style="color: #b71105; margin-top: 20px">Name Can't Contain Numbers!</p>`;
    return;
  } else {
    // after finishing the validation we save the name of the user in our local storage and display an error message if another user 
    // enters the same name that we have in our local storage
    const getName = JSON.parse(localStorage.getItem("names") || "[]");
    if (!getName.includes(nameInput.value?.trim())) {
      saveNameToStorage(nameInput.value?.trim());

    } else if(getName.includes(nameInput.value?.trim())) {
      loginError.innerHTML = `<p style="color: #b71105; margin-top: 20px">This Name Already Exists!</p>`; 
      return;
} 
  

  }
document.querySelector("#form").submit()

});
