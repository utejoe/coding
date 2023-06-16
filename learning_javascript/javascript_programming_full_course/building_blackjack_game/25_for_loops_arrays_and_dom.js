let sentence = ["Hello", "my", "name", "is", "Uyi"]
let greetingEl = document.getElementById("greeting-el")

// How do you keep the spaces between the words (elements) in an array if spaces were not intial added
for (let i = 0; i< sentence.length; i++) {
    greetingEl.textContent += sentence [i] + " "
}