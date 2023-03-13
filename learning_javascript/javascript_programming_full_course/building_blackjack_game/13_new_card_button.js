let firstCard = 10
let secondCard = 7
let sum = firstCard + secondCard
let hasBlackJack = false
let isAlive = true
let message = ""
let messageEl = document.getElementById("message-el")
let sumEl = document.querySelector("#sum-el")
let cardsEl = document.querySelector("#cards-el")

function startGame() {
   if (sum <= 20) {
        message ="Do you want to draw a new card? "
    } else if (sum === 21) {
        message = "Wohoo! YOu've got Blackjack! "
        hasBlackJack = true
    } else {
        message ="YOu're out of the game! "
        isAlive = false
     }
  messageEl.textContent = message
    sumEl.innerText = "Sum = "+sum
    cardsEl.textContent ="firstCards: " + firstCard + ";  secondCard: "+ secondCard
}

// 2. Create a function newCard() that logs out "Drawing a new card"
function newCard() {
    console.log("Drawing a new card from the deck!")    
}
  