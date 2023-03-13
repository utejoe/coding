// the logical OR (||) will run if at least one of the statement is true or false, base on the conditon of the statement
let hasCompletedCourse = true
let givesCertificate = true

if (hasCompletedCourse === true || givesCertificate === false) {
    generateCertificate()
}

function generateCertificate() {
    console.log('Generating certificate....')
}

// Create two boolean variables, likesDocumentaries and likesStartups
// Use an OR (||) to call recommendMovie() if either of those variables are true
let likesDocumentaries= true
let likesStartups = true
if(likesDocumentaries === true || likesStartups === false) {
    recommendMovie()
}
function recommendMovie() {
    console.log(        )// giving space b/w the two print out statement
    console.log("Hey, check out this new film we think you will like!")
}