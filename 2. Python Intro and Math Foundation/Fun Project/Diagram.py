import turtle
from SnowPerson import SnowPerson
from SnowMan import SnowMan
from SnowLady import SnowLady

class Diagram(object):

    def __init__(self):
        pass

    def __str__(self):
        print("~ Thank you ~")
    
    def draw(self):
        print("""
        #####################################
        #                                   #
        #                                   #
        #          Tech Know School         #
        #                                   #
        #                                   #
        #####################################
        """)
        while True:
            a = int(input("1. Snow Person \n2. Snow Man \n3. Snow Lady \n4. Exit \nEnter any input : "))
            if a == 1:
                posX = int(input("Enter the X - cordinate : "))
                posY = int(input("Enter the Y - cordinate : "))
                sp = SnowPerson(posX,posY)
                sp.__str__()
                sp.draw()
            elif a == 2:
                posX = int(input("Enter the X - cordinate : "))
                posY = int(input("Enter the Y - cordinate : "))
                sm = SnowMan(posX,posY)
                sm.__str__()
                sm.draw()
            elif a == 3:
                posX = int(input("Enter the X - cordinate : "))
                posY = int(input("Enter the Y - cordinate : "))
                sl = SnowLady(posX,posY)
                sl.__str__()
                sl.draw()
            elif a == 4:
                d.__str__()
                turtle.getscreen()._root.mainloop()
                break
            else:
                print("please give a correct input")

d = Diagram()
d.draw()
