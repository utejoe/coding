let firstCared = 10
let secondCard = 11
let sum = firstCared + secondCard
let isAlive = true
// 1. Create a varible called isAlive and assign it to true

// 2. Flip its value to false in the appropriate code block
if (sum <= 20) {
    console.log("Do you want to draw a new card? ")
    isAlive = false
} else if (sum === 21) {
    console.log("Wohoo! You've got Blackjack! ")
    
} else {
    console.log("You're out of the game! ")
    isAlive = false
}
console.log(isAlive)