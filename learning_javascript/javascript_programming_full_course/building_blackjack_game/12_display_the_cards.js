let firstCard = 10
let secondCard = 7
let sum = firstCard + secondCard
let hasBlackJack = false
let isAlive = true
let message = ""
let messageEl = document.getElementById("message-el")
let sumEl = document.querySelector("#sum-el")
// 2. Store the cards pargraph in a variable called cardsEl
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
  //3. Render the cards on the page using this format -> "Cards: 10 4"
    messageEl.textContent = message
    sumEl.innerText = "Sum = "+sum
    cardsEl.textContent ="firstCards: " + firstCard + ";  secondCard: "+ secondCard
}