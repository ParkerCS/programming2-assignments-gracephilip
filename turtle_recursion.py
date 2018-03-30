'''
Turtle Recursion (33pts)

1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (15pts)
'''
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.shape("turtle")
my_turtle.showturtle()
my_screen = turtle.Screen()

my_screen.bgcolor("white")

def recursive_hfractal(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size / 2, y)
        my_turtle.goto(x - size / 2, y)
        my_turtle.up()
        my_turtle.goto(x + size / 2, y + size / 2)
        my_turtle.down()

        my_turtle.goto(x + size / 2, y - size / 2)

        my_turtle.up()
        my_turtle.goto(x - size / 2, y + size / 2)
        my_turtle.down()
        my_turtle.goto(x - size / 2, y - size / 2)

        recursive_hfractal(x + size / 2, y + size / 2, size / 2, depth - 1)
        recursive_hfractal(x + size / 2, y - size / 2, size / 2, depth - 1)

        recursive_hfractal(x - size / 2, y - size / 2, size / 2, depth - 1)
        recursive_hfractal(x - size / 2, y + size / 2, size / 2, depth - 1)


recursive_hfractal(0, 0, 300, 1)



my_screen.clear()

'''
2)  Using the turtle library, create any of the other recursive patterns in the data folder. 
Challenge yourself to match your pattern as closely as you can to the image.  (15pts)
Note:  The Koch snowflake shows step by step building of the fractal.  
       The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)
'''
my_turtle.hideturtle()
def koch_fractal(size, depth, my_turtle, depth_init):
    if depth > 0:
        my_turtle.down()
        my_turtle.begin_fill()
        my_turtle.forward(size / 2)
        my_turtle.left(120)
        #my_turtle.up()
        my_turtle.forward(size)
        my_turtle.left(120)
        my_turtle.forward(size)
        my_turtle.left(120)
        my_turtle.forward(size / 2)
        my_turtle.end_fill()
        #my_turtle.down()

        if depth == depth_init:
            my_turtle.left(180)
            my_turtle1 = my_turtle.clone()
            koch_fractal(size / 2, depth - 1, my_turtle1, depth_init)

            my_turtle.left(180)

        my_turtle.up()
        my_turtle.forward(size / 2)
        my_turtle.left(120)
        my_turtle.forward(size / 2)
        my_turtle.right(180)
        my_turtle2 = my_turtle.clone()
        koch_fractal(size / 2, depth - 1, my_turtle2, depth_init)

        my_turtle.up()
        my_turtle.left(180)
        my_turtle.forward(size / 2)
        my_turtle.left(120)
        my_turtle.forward(size / 2)
        my_turtle.left(180)
        my_turtle3 = my_turtle.clone()
        koch_fractal(size / 2, depth - 1, my_turtle3, depth_init)


my_turtle.up()
my_turtle.goto(0, -150)
koch_fractal(300, 6, my_turtle, 6)
my_screen.exitonclick()








'''
3)  Create your own work of art with a repeating pattern of your making.  
It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  
Take this one as seriously as the points indicate.  Play around.  (3pt) 

Give all your fractals a depth of at least 4.  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
All three recursive drawings can be on the same program.  Just use screen.clear() between problems.
 Have fun!
 
 Resource to help you out >>> https://docs.python.org/3.3/library/turtle
'''
