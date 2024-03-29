import pygame
from datetime import datetime

pygame.init()

width, height = 800, 800

display = pygame.display.set_mode((width, height))

pygame.display.set_caption("MicMouse Clock")

second = pygame.image.load("left.png")
minute = pygame.image.load("right.png")
mickey = pygame.image.load("mainclock.png")

mickeyrect = mickey.get_rect(center=(width // 2, height // 2))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    current_time = datetime.now().time()
    second_angle = current_time.second * 6
    minute_angle = current_time.minute * 6 + current_time.second / 10  

    display.fill((255, 255, 255))

    display.blit(mickey, mickeyrect)

    rotated_second_hand = pygame.transform.rotate(second, -second_angle)
    second_hand_rect = rotated_second_hand.get_rect(center=mickeyrect.center)
    display.blit(rotated_second_hand, second_hand_rect)

    rotated_minute_hand = pygame.transform.rotate(minute, -minute_angle)
    minute_hand_rect = rotated_minute_hand.get_rect(center=mickeyrect.center)
    display.blit(rotated_minute_hand, minute_hand_rect)

    pygame.display.flip()

    clock.tick(30)