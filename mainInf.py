import turtle
import fibo

t = turtle.Turtle()
turtle.bgcolor("#0040ff")
t.pencolor("white")
t.pensize(2)
fibo = fibo.get(22)
count = 0
for i in fibo:
    print(f"iter: {i}")
    if i == 1:
        t.forward(25+ count)
    elif i%2 == 0:
        t.right(90)
        t.forward(25+ count)
    else:
        t.left(90)
        t.forward(25+ count)
    count+= 0

turtle.exitonclick()