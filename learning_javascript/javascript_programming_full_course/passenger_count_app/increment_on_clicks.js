// document getElementById("count").innerText = 5

// change the count-el in the HTML  to reflect the new count

// camelCase
let countEl = document.getElementById("count-el")
let savedValue = document.getElementById('saved')

console.log(countEl)

let count = 0

const increment=() =>countEl.innerText = count++
const save =()=> savedValue.innerText = count 