import json
f = open("car.json")
car = json.load(f)
print(car)
print(type (car))
print(car.keys())
print(car['mycar'])
print(car['mycar']['model'])
print(car['mycar']['features'])
