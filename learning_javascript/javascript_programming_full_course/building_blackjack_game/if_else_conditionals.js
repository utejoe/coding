let firstCard = 12
let secondCard = 9
let sum = firstCard + secondCard

if (sum < 21) {
    console.log ("Do you want to draw a new card? 🤨")
} else if (sum === 21) {
    console.log ("Wohoo! you've got Blackjack! 😃")
} else {
    console.log("YOu're out of the game! 😥")
}