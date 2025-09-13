import turtle
t = turtle.Turtle()
t.color("blue")
t.width(5)
t.forward(100)
t.left(120)
t.forward(100)
t.home()
t.pos()
#turtle.clearscreen()
for steps in range(5):
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(steps)
        t.right(30)
#turtle.done()

f = turtle.Turtle()
f.color('red')
f.fillcolor('yellow')
while True:
    f.forward(200)
    f.left(170)
    if abs(f.pos()) < 1:
        break
f.end_fill()
turtle.done()