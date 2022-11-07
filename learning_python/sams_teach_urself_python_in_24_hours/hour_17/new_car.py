from car import Car
mycar = Car(make="Ford", model="Explorer", transmission="automatic", color="red", doors="4", features={"stowaway-seats": True})
print(vars(mycar))
import json
f = open('newcar.json', 'w')
json.dump(vars(mycar), f, indent=2)
f.close()