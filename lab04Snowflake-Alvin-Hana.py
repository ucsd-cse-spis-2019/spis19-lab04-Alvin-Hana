import turtle
def snowflakeSide(sideLength, levels):
    if levels==1:
        t.forward(sideLength)
    else:
        snowflakeSide(sideLength/3, levels-1)
        t.left(60)
        snowflakeSide(sideLength/3, levels-1)
        
        #t.forward(sideLength/3)
        #t.left(60)
        #snowflakeSide(sideLength/3, levels-1)
        t.right(120)
        snowflakeSide(sideLength/3, levels-1)
        t.left(60)
        snowflakeSide(sideLength/3, levels-1)
        #t.forward(sideLength/3)
def snowflake(sideLength, levels):
    global counter 
    counter = 1
    while counter <= 3:
        snowflakeSide(sideLength, levels)
        t.right(120)
        counter+=1
t = turtle.Turtle()
snowflake(280, 4)
turtle.done()

