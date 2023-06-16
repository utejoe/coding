let firstCared = 10
let secondCard = 11
let sum = firstCared + secondCard + 4
let hasBlackJack = false
let isAlive = true
let message = ""


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
    
    console.log(message)
}