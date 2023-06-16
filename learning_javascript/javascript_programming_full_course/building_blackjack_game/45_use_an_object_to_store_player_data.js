// 2. Create the player object. Give it two keys, name and chips,
let player = {
    name : "Obazee Uyi",
    chips : 3000
}
let cards = []
let sum = 0
let hasBlackJack = false
let isAlive = false
let message = ""
let messageEl = document.getElementById("message-el")
let sumEl = document.querySelector("#sum-el")
let cardsEl = document.querySelector("#cards-el")
// 3. Grab ahold of the player-el paragraph and store it in a variable caled playerEL
let playerEl = document.getElementById("player-el")

// 4. Render the player's name and chips in playerEl
playerEl.textContent = player.name + ": $" + player.chips 

function  getRandomCard() {
    let randomNumber = Math.floor(Math.random()*13 + 1)
    if (randomNumber=== 1) {
        return 11 
    } else if (randomNumber >= 11) {
        return 10
    } else {
        return randomNumber
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
    if (hasBlackJack === false && isAlive === true) {
        let card = getRandomCard()
        sum += card
        cards.push(card)
        console.log(cards)
        renderGame()    
    }
   
}

  