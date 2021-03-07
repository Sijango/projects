import time
import turtle
import random


BREAK_FLAG = False

# window
screen = turtle.Screen()
screen.title('Snake with turtle module')
screen.bgcolor('orange')
screen.setup(650, 650)
# screen.tracer(0)

# draw a game field border
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-311, 311)
border.pendown()
border.goto(311, 311)
border.goto(311, -311)
border.goto(-311, -311)
border.goto(-311, 311)

snake = []
for i in range(3):
    snake_segment = turtle.Turtle()
    snake_segment.shape('square')
    snake_segment.penup()
    if i > 0:
        snake_segment.color('gray')
    # snake_segment.speed(10)
    snake.append(snake_segment)

# draw a food for the snake
food = turtle.Turtle()
food.speed(10)
food.shape('circle')
food.penup()
food.goto(random.randrange(-300, 300, 20), random.randrange(-300, 300, 20))

# snake control
screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
screen.listen()

while True:
    # creating a new segment of the snake
    # and redraw a food for the snake
    if snake[0].distance(food) < 10:
        food.goto(random.randrange(-300, 300, 20), random.randrange(-300, 300, 20))
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.color('gray')
        snake_segment.penup()
        # snake_segment.speed(7)
        snake.append(snake_segment)

    # snake body movement
    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x, y)

    # snake head movement
    snake[0].forward(20)
    screen.update()

    # snake collision with border
    x_cor = snake[0].xcor()
    y_cor = snake[0].ycor()
    if x_cor > 300 or x_cor < -300:
        screen.bgcolor('red')
        break
    if y_cor > 300 or y_cor < -300:
        screen.bgcolor('red')
        break

    # snake collision with itself
    for i in snake[1:]:
        i = i.position()
        if snake[0].distance(i) < 10:
            BREAK_FLAG = True
    if BREAK_FLAG:
        screen.bgcolor('red')
        break

    time.sleep(0.07)

screen.exitonclick()
screen.mainloop()