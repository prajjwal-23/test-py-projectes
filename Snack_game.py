import pygame
import random

pygame.init()
# color
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snack Game")
pygame.display.update()
# to track time 
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)


def text_screen(text, color, x, y):
    screen_text = font.render(text,True , color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x ,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game loop
def gameLoop():
    # Game specific veriables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60

    # Creating a Game Loop
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -init_velocity
                    elif event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            # abs() gives us a absalute value 
            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=1
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length +=5


            gameWindow.fill(white)
            text_screen("Score: "+ str(score*10) , red , 5 ,5 )
            # (where, color,list of size and potion)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            # pygame.draw.rect(gameWindow, black, [snake_x,snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        # flip by using tick
        clock.tick(fps)

    pygame.quit()
    quit()

gameLoop()