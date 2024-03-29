import pygame
import os
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((730,360))
bg = pygame.image.load('img/bg.jpg')

clock = pygame.time.Clock()



index = 0
songs = ['Kalimba.mp3', 'Maid with the Flaxen Hair.mp3', 'Sleep Away.mp3']

pygame.mixer.music.load(songs[index])
pygame.mixer.music.play()

play = True

running = True
while running:

    screen.blit(bg, (0,-25))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(1000)  

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        play = not play
        if play:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

    if pressed[pygame.K_LEFT]: 
        index = (index - 1) % len(songs)
        pygame.mixer.music.load(songs[index])
        pygame.mixer.music.play()
        play = True
    
    if pressed[pygame.K_RIGHT]: 
        index = (index + 1) % len(songs)
        pygame.mixer.music.load(songs[index])
        pygame.mixer.music.play()
        play = True

    pygame.display.update()



pygame.quit()