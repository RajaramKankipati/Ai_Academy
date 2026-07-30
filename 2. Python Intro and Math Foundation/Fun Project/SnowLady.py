import turtle
from SnowPerson import SnowPerson
from Triangle import Triangle
from Circle import Circle


class SnowLady(SnowPerson):

    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY

    def __str__(self):
        print("Snow Lady Position : [" + str(self.posX) + ", " +str(self.posY) +"]")

    def draw(self):
        if int(turtle.heading()) == 180:
            turtle.right(180)
        
        #snowperson drawing
        sn = SnowPerson(self.posX,self.posY)
        sn.draw()
        #SnowMan Features
        #Hair and hat
        #left
        x = self.posX
        y = self.posY
        turtle.pen(pencolor="brown",pensize=2)
        turtle.up()
        p = x - 20
        q = y + 55
        turtle.setposition(p,q)
        turtle.down()
        q = y
        p = x - 40
        turtle.setposition(p,q)
        turtle.up()
        p = x - 15
        q = y + 55
        turtle.setposition(p,q)
        turtle.down()
        q = y + 18
        p = x - 28
        turtle.setposition(p,q)
        #right
        turtle.up()
        p = x + 20
        q = y + 55
        turtle.setposition(p,q)
        turtle.down()
        q = y
        p = x + 40
        turtle.setposition(p,q)
        turtle.up()
        p = x + 15
        q = y + 55
        turtle.setposition(p,q)
        turtle.down()
        q = y + 18
        p = x + 28
        turtle.setposition(p,q)
        #hat
        p = x 
        q = y + 110
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        t = Triangle(p,q)
        t.draw()
        #lips
        p = x 
        q = y + 17.5
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        turtle.pen(fillcolor="red",pencolor="red",pensize=1)
        turtle.begin_fill()
        turtle.circle(3)
        turtle.end_fill()
        turtle.pen(fillcolor="",pencolor="black",pensize=2)
        #body items
        p = x 
        q = y - 15
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(7,"yellow")
        c.draw()
        p = x 
        q = y - 55
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(7,"violet")
        c.draw()
        #base items
        p = x 
        q = y - 125
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(7,"yellow")
        c.draw()
        p = x 
        q = y - 180
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(7,"violet")
        c.draw()
        #turtle.getscreen()._root.mainloop()

#sl = SnowLady(130,130)
#sl.draw()
