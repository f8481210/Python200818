import turtle

n = int(input("幾邊形:"))
for i in range(n):
    turtle.forward(100)
    turtle.left(360/n)