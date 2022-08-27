import turtle
import fibo

n = int(input(">. "))


t = turtle.Turtle()
turtle.bgcolor("#0066ff")
t.pencolor("white")
# t.pensize(10)

t.shape('circle')
t.shapesize(0.5)


points = {}

for i in range(n):
    i+=1
    points[i] = round(360/n) * i
points[points.__len__()] = points[points.__len__()] - 1;

print("points: ", points)

pointArr = []
for i in points:
    pointArr.append(points[i])

print("pointsArr: ", pointArr)


t.speed(4)
for i in range(360):
    t.right(1);
    if t.heading() in pointArr:
        points[pointArr.index(t.heading())+1] = t.pos();
        t.clone()
    t.forward(1);


print("points<vec 2d>", points)

t.ht()
fibo = fibo.getMod(n, 64);
print("Modulated Fibonacci: ", fibo)

for i in fibo:
    for j in points:
        if i == j-1:
            t.goto(points[j])
            break;


turtle.exitonclick()