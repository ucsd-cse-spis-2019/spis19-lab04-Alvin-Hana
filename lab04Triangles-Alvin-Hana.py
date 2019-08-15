import turtle
def triangles(sideLength, levels):
    if levels == 0:
        pass
    else:
        t.forward(sideLength)
        t.left(120)
        t.forward(sideLength)
        t.left(120)
        t.forward(sideLength)
        t.left(120)
        triangles(sideLength/2, levels-1)
        t.forward(sideLength/2)
        triangles(sideLength/2, levels-1)
        t.back(sideLength/2)
        t.left(60)
        t.forward(sideLength/2)
        t.right(60)
        triangles(sideLength/2, levels-1)
        t.left(60)
        t.back(sideLength/2)
        t.right(60)

t=turtle.Turtle()
t.speed(0)
triangles(400,6)
turtle.done()
