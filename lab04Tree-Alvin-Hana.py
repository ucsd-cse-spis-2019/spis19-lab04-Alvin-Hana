import turtle
def tree (trunkLength, height):
    if height == 0:
        pass
    else:
        t.forward(trunkLength)
        t.left(45)
        tree(trunkLength/2, height-1)
        t.right(90)
        tree(trunkLength/2, height-1)
        t.left(45)
        t.back(trunkLength)

       
t = turtle.Turtle()
t.speed(4)
t.left(90)
tree(200, 4)
turtle.done()

