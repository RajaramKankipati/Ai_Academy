import turtle

class Circle(object):

    def __init__(self,radius,fillColor):
        self.radius = radius
        self.fillColor = fillColor
        
    def __str__(self):
        pass

    def draw(self):      
        turtle.color("black", self.fillColor)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()
        
        

