#檔名:turtle02
import turtle
#import time

a = turtle.Turtle() #創造一個叫a的烏龜
b = turtle.Turtle()

a.color('blue')
b.color('yellow')

a.pensize(10)
b.pensize(5)

for i in range(361):
    a.forward(1)
    #time.sleep(1)
    a.left(1)
for j in range(361):
    b.forward(1)
    #time.sleep(1)
    b.right(1)
    

turtle.done()