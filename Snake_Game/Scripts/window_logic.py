import random
import turtle

from Scripts.status import Status


class Window:
    def __init__(self):
        self.screen = turtle.Screen()
        self.border = turtle.Turtle()
        self.food = turtle.Turtle()

        self.game_status = Status.WAIT_FLAG

        self.border.speed(10)   # set speed drawing border
        self.food.speed(10)     # set speed drawing food

    def init_screen(self):
        self.screen.title('Snake Game')
        self.screen.bgcolor('orange')
        self.screen.setup(650, 650)

    def init_border(self):
        self.border.hideturtle()
        self.border.penup()
        self.border.goto(-311, 311)
        self.border.pendown()
        self.border.goto(311, 311)
        self.border.goto(311, -311)
        self.border.goto(-311, -311)
        self.border.goto(-311, 311)

    def init_food(self):
        self.food.shape('circle')
        self.food.penup()
        self.food.goto(random.randrange(-300, 300, 20), random.randrange(-300, 300, 20))

    def init_snake_click(self, snake):
        self.screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
        self.screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
        self.screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
        self.screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
        self.screen.listen()

    def check_death_window(self):
        if self.game_status == Status.END_FLAG:
            self.screen.bgcolor('red')
            return False
        return True

    def exit(self):
        self.screen.mainloop()
        self.screen.exitonclick()

