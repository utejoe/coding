import turtle

class polygon:
    def __init__(self, sides, name, size=100, color="black", line_thickness=2):
        self.sides = sides
        self.name = name
        self.size = size  
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

    def draw(self): 
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180-self.angle)
        turtle.done()

def draw_function(sides, size, angle, line_thickness, color):
    turtle.color(color)
    turtle.pensize(line_thickness)
    for i in range(sides):
        turtle.forward(100)
        turtle.right(180-angle)
    turtle.done()



square = polygon(4, 'Square', 10)
pentagon = polygon(5, "Pentagon")
 
  
print(square.sides)
print(square.name)

print(pentagon.sides)   
print(pentagon.name)

hexagon = polygon(6, "Hexagon", color='red',)
#hexagon.draw()
draw_function(5, 100, 108, 4, "blue") 