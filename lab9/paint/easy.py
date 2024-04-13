import pygame
import math

queue = []

def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)


def step(screen, x, y, origin_color, fill_color): #checking borders, color and putting coordinates in a queue
    if x < 0 or y < 0: return False
    if x > 400 or y > 300: return False
    if screen.get_at((x, y)) != origin_color: return False
    queue.append((x, y))
    screen.set_at((x, y), fill_color)


pygame.init()
screen = pygame.display.set_mode((400, 300))
another_layer = pygame.Surface((400, 300))

done = False
clock = pygame.time.Clock()

origin_color = (0, 0, 0)
fill_color = (255, 0, 0)

tool = 0
# 0 - pencil
# 1 - rectangle
# 2 - fill
# 3 - square
# 4 - right triangle
# 5 - equilateral triangle
# 6 - rhombus

tools_count = 7

x1 = 10
y1 = 10
x2 = 10
y2 = 10

w = 100
h = 100
color = (0, 128, 255)
isMouseDown = False
screen.fill((0, 0, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                if tool == 0:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    x2 = x1
                    y2 = y1
                elif tool == 1:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                elif tool == 2:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    origin_color = screen.get_at((x1, y1))
                    queue.append((x1, y1))
                    screen.set_at((x1, y1), fill_color)

                    while len(queue) > 0:
                        cur_pos = queue[0]
                        queue.pop(0)
                        step(screen, cur_pos[0] + 1, cur_pos[1], origin_color,  fill_color)
                        step(screen, cur_pos[0] - 1, cur_pos[1], origin_color, fill_color)
                        step(screen, cur_pos[0], cur_pos[1] + 1, origin_color, fill_color)
                        step(screen, cur_pos[0], cur_pos[1] - 1, origin_color, fill_color)
                elif tool == 3:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    x2 = x1
                    y2 = y1
                elif tool == 4:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    x2 = x1
                    y2 = y1
                elif tool == 5:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    x2 = x1
                    y2 = y1
                elif tool == 6:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    x2 = x1
                    y2 = y1

            elif event.button == 3:  # right click
                tool = (tool + 1) % tools_count
            isMouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                another_layer.blit(screen, (0, 0))
            isMouseDown = False

        if event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                if tool == 0:
                    x1 = x2
                    y1 = y2
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    pygame.draw.line(screen, color, (x1, y1), (x2, y2))
                elif tool == 1:
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    pygame.draw.rect(screen, color, pygame.Rect(getRectangle(x1, y1, x2, y2)), 1)
                elif tool == 3:
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    side_length = max(abs(x2 - x1), abs(y2 - y1))
                    if x2 < x1:
                        x1 = x2
                    if y2 < y1:
                        y1 = y2
                    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, side_length, side_length), 1)
                elif tool == 4:
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    pygame.draw.polygon(screen, color, [(x1, y1), (x2, y1), (x1, y2)], 1)
                elif tool == 5:
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    side_length = math.hypot(x2 - x1, y2 - y1)
                    height = (math.sqrt(3) / 2) * side_length
                    apex_x = (x1 + x2) / 2
                    apex_y = y1 - height
                    pygame.draw.polygon(screen, color, [(x1, y1), (x2, y1), (apex_x, apex_y)], 1)
                elif tool == 6:
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    dx = (x2 - x1)
                    dy = (y2 - y1)
                    mid_x = (x1 + x2) / 2
                    mid_y = (y1 + y2) / 2
                    pygame.draw.polygon(screen, color, [(mid_x - dx, mid_y), (mid_x, mid_y - dy), (mid_x + dx, mid_y), (mid_x, mid_y + dy)], 1)

   

    pygame.display.flip()
    clock.tick(60)
