// Create a person object that contains three keys: name, age, and country.
// Use yourself as an example to set the values for name, age, and country.
let person = {
    name: "Uyi",
    age: 18,
    country: "Nigeria"
}
// Create a function, logData(), that uses the person object to create a 
// string in the floowing format:
// "Uyi is 18 years old and lives in Nigeria"
function logData() {
console.log(person.name + " is " + person.age + " years old and lives in "+ person.country)
}

// Call the logData() function to verify that it works
logData()