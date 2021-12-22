import turtle as tl

def draw_fractal(size):
    if size >= 12:
        tl.pensize(max(size / 30, 1))
        tl.forward(size)
        tl.left(25)
        draw_fractal(size / 1.5)
        tl.right(50)
        draw_fractal(size / 1.5)
        tl.left(25)
        draw_fractal(size / 2)
        tl.penup()
        tl.backward(size)
        tl.pendown()
    else:
        tl.pensize(3)
        
size = 200

tl.delay(1)
tl.speed(0)
tl.penup()
tl.color('green')
tl.goto(0, -size * 2)
tl.setheading(90)
tl.pendown()

draw_fractal(size)
tl.done()





