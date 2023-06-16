// check the file render_welcome_message for more understanding

let welcomeEl = document.getElementById("welcome-el")
let greeting = "welcome back "

welcomeEl.innerText = greeting + name

// Add an emoji to the end! 
// WRITE YOUR CODE BELOW HERE
// HINT: count = count + 1

welcomeEl.innerText = welcomeEl.innerText + "😁"