let num1 = 8
let num2 = 2
document.getElementById("num1-el").textContent = num1
document.getElementById("num2-el").textContent = num2

// Create four functions: add(), subract(), divide(), multiply()
// Call the correct function when the user clicks on one of the buttons
// Perform the given calculation using num1 and num2
// Render the result of the calculation in the paragraph with id="sum-el"

// e.g. if the user  clicks on the "Plus" button, you should render
// "sum: 10" (since 8+2 = 20) inside the paragraph with id="sum-el"
let sumEl = document.getElementById("sum-el")

function add() {
    let result = num1 + num2
    sumEl.textContent = "sum: "+ result
}

function subtract() {
    let result = num1 - num2
    sumEl.textContent = "sub: "+ result
}

function divide() {
    let result = num1 / num2
    sumEl.textContent = "divide: "+ result
}

function multiply() {
    let result = num1 * num2
    sumEl.textContent = "times: "+ result
}