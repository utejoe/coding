let firstCard = getRandomCard()
let secondCard = getRandomCard()
cards = [firstCard, secondCard]
let sum = firstCard + secondCard
let hasBlackJack = false
let isAlive = true
let message = ""
let messageEl = document.getElementById("message-el")
let sumEl = document.querySelector("#sum-el")
let cardsEl = document.querySelector("#cards-el")


function  getRandomCard() {
    // if 1     -> return 11
    // if 11-13 -> return 10
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
    let card = getRandomCard()
    sum += card
    cards.push(card)
    console.log(cards)
    renderGame()
}
  