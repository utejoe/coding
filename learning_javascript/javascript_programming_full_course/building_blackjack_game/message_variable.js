let firstCared = 10
let secondCard = 11
let sum = firstCared + secondCard + 4
let hasBlackJack = false
let isAlive = true
// 1. Declare a variable called message and assign its value to an empty string

// 2. Reassign the message variable to the string we're logging out
if (sum <= 20) {
    console.log("Do you want to draw a new card? ")
} else if (sum === 21) {
    console.log("Wohoo! YOu've got Blackjack! ")
    hasBlackJack = true
} else {
    console.log("YOu're out of the game! ")
    isAlive = false
}

// 3. Log it out!