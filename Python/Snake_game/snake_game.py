import curses
import random

screen = curses.initscr()

curses.curs_set(0)

scrren_height, screen_width = screen.getmaxyx()

window = curses.newwin(scrren_height, screen_width, 0, 0)

window.keypad(True)

window.timeout(300)

snake_x = screen_width // 4
snake_y = scrren_height // 2
#define the initial position of the snake body.
snake = [[snake_y, snake_x], [snake_y, snake_x - 1], [snake_y, snake_x - 2]]
#create the food in middle of the window
food = [scrren_height // 2, screen_width // 2]
#add a character in a window
window.addch(food[0], food[1], curses.ACS_BULLET)
#set the initial movment direction
key = curses.KEY_RIGHT

while True:
  #get the next key from the user
  next_key = window.getch()
  key = key if next_key == -1 else next_key
  #check if snake collided in a wall or itself
  if snake[0][0] in [0, scrren_height] or snake[0][1] in [
      0, screen_width
  ] or snake[0] in snake[1:]:
    curses.endwin()
    quit()
#set the new position of the snake head
  new_head = [snake[0][0], snake[0][1]]
  if key == curses.KEY_DOWN:
    new_head[0] += 1
  if key == curses.KEY_UP:
    new_head[0] -= 1
  if key == curses.KEY_RIGHT:
    new_head[1] += 1
  if key == curses.KEY_LEFT:
    new_head[1] -= 1
#insert the new head to first position of the snake list
  snake.insert(0, new_head)
  #cheeck if the snake ate the food
  if snake[0] == food:
    food = None
    # generate a new food in a random position
    while food is None:
      new_food = [
          random.randint(1, scrren_height - 1),
          random.randint(1, screen_width - 1)
      ]
      food = new_food if new_food not in snake else None
    window.addch(food[0], food[1], curses.ACS_BULLET)
  else:
    tail = snake.pop()
    window.addch(tail[0], tail[1], ' ')

  window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
