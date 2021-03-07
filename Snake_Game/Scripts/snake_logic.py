import random
import turtle

from Scripts.status import Status


class Snake:
    def __init__(self):
        self.snake = []

    def init_snake(self):
        for i in range(3):
            snake_segment = turtle.Turtle()
            snake_segment.shape('square')
            snake_segment.penup()
            if i > 0:
                snake_segment.color('gray')
            # snake_segment.speed(10)
            self.snake.append(snake_segment)

    def check_collision_with_border(self, screen):
        x_cor = self.snake[0].xcor()
        y_cor = self.snake[0].ycor()

        if x_cor > 300 or x_cor < -300:
            screen.game_status = Status.END_FLAG

        if y_cor > 300 or y_cor < -300:
            screen.game_status = Status.END_FLAG

    def check_collision_with_itself(self, screen):
        for i in self.snake[1:]:
            i = i.position()
            if self.snake[0].distance(i) < 10:
                screen.game_status = Status.END_FLAG

    def check_collision_with_food(self, food):
        if self.snake[0].distance(food) < 10:
            food.goto(random.randrange(-300, 300, 20), random.randrange(-300, 300, 20))
            snake_segment = turtle.Turtle()
            snake_segment.shape('square')
            snake_segment.color('gray')
            snake_segment.penup()
            # snake_segment.speed(7)
            self.snake.append(snake_segment)

    def snake_update(self, screen):
        for i in range(len(self.snake) - 1, 0, -1):
            x = self.snake[i - 1].xcor()
            y = self.snake[i - 1].ycor()
            self.snake[i].goto(x, y)

        self.snake[0].forward(20)
        screen.update()
