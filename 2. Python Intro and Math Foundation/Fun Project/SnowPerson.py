import turtle
from Circle import Circle

class SnowPerson(object):

    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY

    def __str__(self):
        print("Snow Person Position : ["+str(self.posX)+", "+str(self.posY)+"]")

    def draw(self):
        #wn = turtle.Screen()
        #t = turtle.Turtle()
        if int(turtle.heading()) == 180:
            turtle.right(180)
        turtle.up()
        turtle.pen(pencolor="black",pensize=2)
        turtle.setposition(self.posX,self.posY)
        x,y = turtle.pos()
        turtle.down()
        #face
        c = Circle(30,"")
        c.draw()
        x,y = turtle.pos()
        x = round(x,3)
        y = round(y,3)
        #right eye
        turtle.up()
        p = x + 6
        q = y + 35
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(3,"blue")
        c.draw()
        #left eye
        turtle.up()
        turtle.setposition(x,y)
        p = x - 6
        q = y + 35
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(3,"blue")
        c.draw()
        #smile
        turtle.up()
        turtle.right(90)
        turtle.setposition(x,y)
        p = x - 6
        q = y + 20
        turtle.setposition(p,q)
        turtle.down()
        turtle.pencolor("red")
        turtle.circle(7,180)
        turtle.pencolor("black")
        #body
        turtle.up()
        turtle.setposition(x,y)
        turtle.left(90)
        turtle.down()
        c = Circle(45,"")
        c.draw()
        #left hand
        turtle.up()
        turtle.pen(pencolor="brown",pensize=5)
        turtle.setposition(x,y)
        p = x - 38
        q = y - 20
        turtle.setposition(p,q)
        turtle.down()
        turtle.setposition(p - 45,q + 20)
        #right hand
        turtle.up()
        turtle.setposition(x,y)
        p = x + 38
        q = y - 20
        turtle.setposition(p,q)
        turtle.down()
        turtle.setposition(p + 45,q + 20)
        #base
        turtle.up()
        turtle.pen(pencolor="black",pensize=2)
        turtle.setposition(x,y)
        p = x
        q = y - 90
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(70,"")
        c.draw()
        

#s = SnowPerson(10,10)
#s.draw()
