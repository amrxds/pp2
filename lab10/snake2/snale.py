import pygame
import time
import random
import csv

# Function to write user scores to a CSV file
def write_score_to_csv(username, score):
    with open('scores.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, score])

print ("Enter your username:")
login=str(input())

# Game settings
snake_speed = 15
window_width = 720
window_height = 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)

# Pygame initialization
pygame.init()
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_width, window_height))
fps = pygame.time.Clock()

# Pause
paused=False
pause_icon = pygame.image.load('пауза.png')
resume_icon = pygame.image.load('resume.png')
icon_rect = pause_icon.get_rect()
icon_rect.center = (window_width // 2 + 20, window_height // 2)

# Snake position and body
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
speed = 0
level = 1 

# Fruit and big fruit positions
fruit_position = [random.randrange(1, (window_width // 10)) * 10-20, random.randrange(1, (window_height // 10)) * 10-20]
big_fruit_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]
walls = []
a=random.randint(20, 100)
b=random.randint(20, 100)

def create_wall():
    wall_position = [random.randrange(1, (window_width // 10)) * 10 - 100, random.randrange(1, (window_height // 10)) * 10 - 100]
    walls.append(wall_position)

def draw_walls():
    for wall in walls:
        pygame.draw.rect(game_window, yellow, pygame.Rect(wall[0], wall[1], a, b))

fruit_spawn = True
big_fruit_spawn = True

fruit_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]

big_fruit_timer = 0
fruit_change_interval = 500  

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(a, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect) 

def show_time(a, color, font, size):
    time_font = pygame.font.SysFont(font, size)
    time_surface = time_font.render("time: "+str(big_fruit_timer) + "/500", True, color)
    time_rect = time_surface.get_rect()
    time_rect.topright = (window_width - 10, 1)
    game_window.blit(time_surface, time_rect)

def show_login(a, color, font, size):
    login_font = pygame.font.SysFont(font, size)
    login_surface = login_font.render("login: "+str(login), True, color)
    login_rect = login_surface.get_rect()
    login_rect.topright = (360, 1)
    game_window.blit(login_surface, login_rect)

def show_level(a, color, font, size):
    level_font = pygame.font.SysFont(font, size)
    level_surface = level_font.render("level: "+str(level), True, color)
    level_rect = level_surface.get_rect()
    level_rect.topright = (500, 1)
    game_window.blit(level_surface, level_rect)

def game_over():
    write_score_to_csv(login, score)  # Write the score to CSV file
    game_over_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = game_over_font.render('Game Over, Your Score is: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_width / 2, window_height / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
   

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'


    if not paused:
             # Avoiding reversing the direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= (10)
        if direction == 'DOWN':
            snake_position[1] += (10)
        if direction == 'LEFT':
            snake_position[0] -= (10)
        if direction == 'RIGHT':
            snake_position[0] += (10)

        big_fruit_timer += fps.get_rawtime()

        if big_fruit_timer > fruit_change_interval:
            big_fruit_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]
            big_fruit_timer = 0

        if snake_position[0] < 0 or snake_position[0] > window_width - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_height - 10:
            game_over()
            
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        if score>=100 and score <200:
            level=2

        if score>=200 and score <300:
            level=3
        
        if score>=300 and score <400:
            level=4

        if score>=400:
            level=5

        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            speed=0.01
            fruit_spawn = False
        else:
            snake_body.pop()
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]

        snake_head_rect = pygame.Rect(snake_position[0], snake_position[1], 10, 10)
        big_fruit_rect = pygame.Rect(big_fruit_position[0], big_fruit_position[1], 15, 15)
        snake_body.insert(0, list(snake_position))
        if snake_head_rect.colliderect(big_fruit_rect):
            random_number = random.randint(10, 20)
            score += random_number
            speed=0.02
            big_fruit_spawn = False
            big_fruit_timer = 0
        else:
            snake_body.pop()
            
        if not big_fruit_spawn:
            big_fruit_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]
            
        fruit_spawn = True
        big_fruit_spawn = True

        game_window.fill(black)
        
        for pos in snake_body:
            pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))
            
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(big_fruit_position[0], big_fruit_position[1], 20, 20))

        if score % 100 == 0 and score != 0 and score // 100 > len(walls):
            create_wall()

        show_score(1, white, 'times new roman', 20)
        show_time(1, red, 'times new roman', 20)
        show_login(1, white, 'times new roman', 20)
        show_level(1, white, 'times new roman', 20)
        
    if paused:
        game_window.blit(resume_icon if paused else pause_icon, icon_rect)
   
    pygame.display.update()

    draw_walls()

    snake_speed+=speed

    fps.tick(snake_speed)