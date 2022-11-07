import json
f = open('car.json')
car = json.load(f)
f.close()
car['mycar']['color'] = 'red'
f = open('car.json', 'w')
json.dump(car, f)
print( f.close())
