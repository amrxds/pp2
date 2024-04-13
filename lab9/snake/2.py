import pygame
from random import randrange

RES = 500
SIZE = 25
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
snake = [(x, y)]
dx, dy = 0, 0
FPS = 5
score = 0
LVL = 1
pygame.init()

sc = pygame.display.set_mode((RES, RES))
clock = pygame.time.Clock()

font = pygame.font.Font('pobeda-regular1.ttf', 35)
eat_sound = pygame.mixer.Sound("eat_sound.wav")

def generate_apples(num_apples):
    apples = []
    for _ in range(num_apples):
        apple_x, apple_y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        apples.append((apple_x, apple_y))
    return apples

apples = generate_apples(3)  # Генерируем три яблока

length = 1  # Определяем переменную для отслеживания длины змеи

last_apple_time = pygame.time.get_ticks()  # Время последнего появления яблока
apple_spawn_interval = 5000  # Интервал времени для появления нового яблока (в миллисекундах)

def update_apples():
    global apples, last_apple_time
    current_time = pygame.time.get_ticks()
    if current_time - last_apple_time >= apple_spawn_interval:
        apples = generate_apples(3)  # Генерируем новые яблоки
        last_apple_time = current_time  # Обновляем время последнего появления яблока

while True:
    sc.fill(pygame.Color('black'))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lvl = font.render(f"LVL: {LVL}", True, (255, 255, 255))
    sc.blit(score_text, (20, 20))
    sc.blit(lvl, (400, 20))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    for apple in apples:
        pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]
    pygame.display.flip()
    clock.tick(FPS)

    update_apples()  # Обновляем позиции яблок

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dx, dy = 0, -1
            elif event.key == pygame.K_s:
                dx, dy = 0, 1
            elif event.key == pygame.K_a:
                dx, dy = -1, 0
            elif event.key == pygame.K_d:
                dx, dy = 1, 0

    for apple in apples:
        if snake[-1] == apple:
            apples.remove(apple)  # Удаляем съеденное яблоко
            length += 1
            score += randrange(1, 3)
            eat_sound.play()
            if score % 4 == 0:
                LVL += 1
                FPS += 0.5
            break

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        end_text = font.render('Game Over', True, (255, 255, 255))
        sc.blit(end_text, (RES // 2 - end_text.get_width() // 2, RES // 2 - end_text.get_height() // 2))
        pygame.display.update()  # Update the display to show the "Game Over" text
        pygame.time.delay(2000)  # Delay for 2 seconds before quitting
        pygame.quit()
        exit()
