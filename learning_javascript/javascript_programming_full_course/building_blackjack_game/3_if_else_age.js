// Check if the person is elegible for a birthday card from the King! (100)

// if less than 100 -> "Not elegible"
// else if exactly 100 -> "Here is your birthday card from the king!"
// else                -> "Not elegible, you have already gotten one"

let age = 105;

if (age < 100) {
    console.log("sorry you're not eligible for card")
} else if (age===100) {
    console.log("here is your card from the king")
} else {
    console.log("you've passed age of receiving a card")
}