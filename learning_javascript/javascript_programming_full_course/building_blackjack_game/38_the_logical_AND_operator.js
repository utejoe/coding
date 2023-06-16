// the logical AND (&&) operator will run if both the variable in the function is false or true 

let hasCompletedCourse = true
let givesCertificate = true

if (hasCompletedCourse === true) {
    if (givesCertificate === true) {
        generateCertificate()
    }
}

function generateCertificate() {
    console.log("Generating certificate....")
}

// or

let hascompletedCourse = false
let givescertificate =false

if (hascompletedCourse === false && givescertificate === false) {
        generateCertificate()
    }


function generateCertificate() {
    console.log("Generating certificate....")
}