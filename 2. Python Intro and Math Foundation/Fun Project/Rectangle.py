import turtle

class Rectangle(object):

    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY

    def __str__():
        pass

    def draw(self):
        turtle.up()
        turtle.setposition(self.posX,self.posY)
        turtle.begin_fill()
        turtle.color("brown")
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.end_fill()
        
