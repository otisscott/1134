import turtle
width = 433
height = 325
ratio = 255/width
img = []
for pix in range(height):
    row = []
    for num in range(width):
        row.append(round(255 - (num * ratio)))
    img.append(row)

turtle.tracer(0,0)
turtle.hideturtle()
for irow in range(len(img)):
    for icol in range(len(img[irow])):
        val = img[irow][icol]
        turtle.up()
        turtle.goto(icol, -irow)
        turtle.down()
        turtle.color((val/255, val/255, val/255))
        turtle.dot(1)
        turtle.update()
