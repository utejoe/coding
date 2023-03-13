// Arrays - ordered lists of items
// note that the numbering of arrays starts from 0

let featuredPosts = [
    "Check out my Netflix clone"    // 0
,"Here's the code for my project",  // 1
"I've just relaunched my portfolio" // 2
] 

console.log(featuredPosts[0], featuredPosts[1])

let experience = ["Ceo at Scrimba", "Frontend developer at Xeneta", "People counter for Norstat"]

// Make the following appear in the console:
// Frontend developer at Xeneta
// People counter for Norstat
// CEO at Scrimba
console.log(experience[1])
console.log(experience[2])
console.log(experience[0])

// knowing how many items in an array.. we use .length (this does not start from 0 but from 1)

console.log(experience.length)