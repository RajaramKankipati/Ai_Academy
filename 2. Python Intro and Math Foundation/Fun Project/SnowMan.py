import turtle
from SnowPerson import SnowPerson
from Rectangle import Rectangle
from Circle import Circle

class SnowMan(SnowPerson):

    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY

    def __str__(self):
        print("Snow Man Position : ["+str(self.posX)+", "+str(self.posY)+"]")

    def draw(self):
        if int(turtle.heading()) == 180:
            turtle.right(180)
        #snowperson drawing
        sn = SnowPerson(self.posX,self.posY)
        sn.draw()
        #SnowMan Features
        #Hat
        x = self.posX
        y = self.posY
        turtle.up()
        p = x - 35
        q = y + 59
        turtle.pen(pencolor="brown",pensize=2)
        turtle.setposition(p,q)
        turtle.down()
        p = x + 35
        turtle.setposition(p,q)
        turtle.up()
        p = x - 19
        turtle.setposition(p,q)
        turtle.down()
        p = x + 15
        r = Rectangle(p,q)
        r.draw()
        #body items
        p = x 
        q = y - 15
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(7,"wheat")
        c.draw()
        p = x 
        q = y - 55
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(7,"wheat")
        c.draw()
        #base items
        p = x 
        q = y - 115
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(7,"wheat")
        c.draw()
        p = x 
        q = y - 155
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(7,"wheat")
        c.draw()
        p = x 
        q = y - 200
        turtle.up()
        turtle.setposition(p,q)
        turtle.down()
        c = Circle(7,"wheat")
        c.draw()
        #turtle.getscreen()._root.mainloop()

#s = SnowMan(10,10)
#s.draw()
