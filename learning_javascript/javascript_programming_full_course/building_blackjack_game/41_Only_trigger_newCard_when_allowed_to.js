let cards = []
let sum = 0
let hasBlackJack = false
let isAlive = false
let message = ""
let messageEl = document.getElementById("message-el")
let sumEl = document.querySelector("#sum-el")
let cardsEl = document.querySelector("#cards-el")

console.log(cards)
function  getRandomCard() {
    let randomCard = Math.floor(Math.random()*13 + 1)
    if (randomCard=== 1) {
        return 11
    } else if (randomCard >= 11) {
        return 10
    } else {
        return randomCard
    }
}

function startGame (){
    isAlive = true 
    let firstCard = getRandomCard()
    let secondCard = getRandomCard()
    cards = [firstCard, secondCard]
    sum = firstCard + secondCard
   renderGame()
}
function renderGame() {
    cardsEl.textContent = "Cards:"
    for (let i = 0; i< cards.length; i++) {
        cardsEl.textContent += cards[i] + " "
    }
    
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
    // Only allow the player to get a new card if she IS alive and does NOT have a BlackJack
    if (hasBlackJack === false && isAlive === true) {
        let card = getRandomCard()
        sum += card
        cards.push(card)
        console.log(cards)
        renderGame()    
    }
   
}
  