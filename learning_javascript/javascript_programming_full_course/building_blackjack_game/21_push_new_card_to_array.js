let firstCard = 10
let secondCard = 4
// 1. Create a new array - cards - that contains firstCard and secondCard
cards = [firstCard, secondCard]
let sum = firstCard + secondCard
let hasBlackJack = false
let isAlive = true
let message = ""
let messageEl = document.getElementById("message-el")
let sumEl = document.querySelector("#sum-el")
let cardsEl = document.querySelector("#cards-el")
function startGame (){
    renderGame()
}

function renderGame() {
    cardsEl.textContent ="firstcard: " + cards[0] + " secondcard: " + cards[1]
    sumEl.innerText = "Sum = "+sum
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
}


function newCard() {
    let card = 7
    sum += card
    // Push the cared to the cards array
    cards.push(card)
    renderGame()
}
  