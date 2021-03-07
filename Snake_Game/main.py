import time

from Scripts.status import Status
from Scripts.window_logic import Window
from Scripts.snake_logic import Snake

screen = Window()
snake = Snake()

screen.init_screen()
screen.init_border()
screen.init_food()

snake.init_snake()
screen.init_snake_click(snake.snake)

screen.game_status = Status.START_FLAG

while screen.check_death_window():
    snake.check_collision_with_food(screen.food)

    snake.snake_update(screen.screen)

    snake.check_collision_with_border(screen)
    snake.check_collision_with_itself(screen)

time.sleep(10)
#screen.exit()

