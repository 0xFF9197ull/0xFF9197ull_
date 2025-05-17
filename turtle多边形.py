"""
######################
#####            #####
##### TURTLE     #####
#####            #####
######################
"""
import turtle
pen = turtle.Pen()
pen.ht()
pen.speed(0)
length = 1
angle = 3
def polygon(self,length,angle):
    for k in range(0,angle):
        self.forward(length)
        self.right(360/angle)
while not (length == angle == 0) :
    length,angle=eval(input("输入长度和边数，用逗号隔开"))
    pen.clear()
    pen.goto(0,0)
    polygon(pen,length,angle)
print("已退出")
