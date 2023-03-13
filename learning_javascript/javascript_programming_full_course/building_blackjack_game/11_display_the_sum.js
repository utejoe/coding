let firstCard = 10
let secondCard = 7
let sum = firstCard + secondCard + 6
let hasBlackJack = false
let isAlive = true
let message = ""
let messageEl = document.getElementById("message-el")
// 2. Store the sum paragraph in a variable called sumEl
let sumEl = document.querySelector("#sum-el")

function startGame() {
    //3. Render the sum on the page using this format -> "Sum: 14"
    if (sum <= 20) {
        message ="Do you want to draw a new card? "
    } else if (sum === 21) {
        message = "Wohoo! YOu've got Blackjack! "
        hasBlackJack = true
    } else {
        message ="YOu're out of the game! "
        isAlive = false
        
    }
// 2. Display the message in the messageEl using messageEl.textContent
    messageEl.textContent = message
    sumEl.innerText = "Sum = "+sum
}