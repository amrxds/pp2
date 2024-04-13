import pygame
from random import randrange

RES = 500
SIZE = 25
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE) #random (от нуля до RES, с шагом size)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE) 
dirs = {'W': True,'S': True,'A': True,'D': True}
length = 1
snake = [(x,y)]
dx, dy = 0,0
FPS = 5
score = 0
LVL = 1
pygame.init()

sc = pygame.display.set_mode((RES, RES))
clock = pygame.time.Clock()

font = pygame.font.Font('pobeda-regular1.ttf',35)
eat_sound = pygame.mixer.Sound("eat_sound.wav")
while True:
    

    sc.fill(pygame.Color('black'))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255)) #сглаживание
    lvl = font.render(f"LVL: {LVL}", True, (255, 255, 255))
    sc.blit(score_text, (20, 20))
    sc.blit(lvl, (400,20))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i,j, SIZE, SIZE))) for i, j in snake] #размерами size x size
    pygame.draw.rect(sc,pygame.Color('red'), (*apple, SIZE, SIZE))

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x,y)) #новая координата
    snake = snake[-length:] #убрать последние ленс из списка
    pygame.display.flip()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True,'S': False,'A': True,'D': True}
            elif event.key == pygame.K_s and dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False,'S': True,'A': True,'D': True}
            elif event.key == pygame.K_a and dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True,'S': True,'A': True,'D': False}
            elif event.key == pygame.K_d and dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True,'S': True,'A': False,'D': True}

    if snake[-1] == apple:  # Check if snake head collides with the apple
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        eat_sound.play()
        if score % 4 == 0:  
            LVL += 1  
            FPS += 0.5
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        end_text = font.render('Game Over', True, (255, 255, 255))
        sc.blit(end_text, (RES // 2 - end_text.get_width() // 2, RES // 2 - end_text.get_height() // 2))
        pygame.display.update()  # Update the display to show the "Game Over" text
        pygame.time.delay(2000)  # Delay for 2 seconds before quitting
        pygame.quit()
        exit()
    