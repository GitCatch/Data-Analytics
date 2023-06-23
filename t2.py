from turtle import*
speed('fastest')
size = 10
angle = 61
colors = ['red','purple','blue','green']
while True:
    pencolor(colors[size%4])
    fd(size)
    lt(angle)
    size += 1