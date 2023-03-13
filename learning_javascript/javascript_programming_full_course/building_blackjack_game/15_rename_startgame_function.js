let firstCard = 10
let secondCard = 4
let sum = firstCard + secondCard
let hasBlackJack = false
let isAlive = true
let message = ""
let messageEl = document.getElementById("message-el")
let sumEl = document.querySelector("#sum-el")
let cardsEl = document.querySelector("#cards-el")

// Create a new function called startGame() that calls renderGame()
function startGame (){
    renderGame()
}
function renderGame() {
   if (sum <= 20) {
        message ="Do you want to draw a new card? "
    } else if (sum === 21) {
        message = "Wohoo! You've got Blackjack! "
        hasBlackJack = true
    } else {
        message ="YOu're out of the game! "
        isAlive = false
     }
  messageEl.textContent = message
    sumEl.innerText = "Sum = "+sum
    cardsEl.textContent ="firstCards: " + firstCard + ";  secondCard: "+ secondCard
}


function newCard() {
    console.log("Drawing a new card from the deck!")    
    let card = 7
    sum += card
    renderGame()
}
  