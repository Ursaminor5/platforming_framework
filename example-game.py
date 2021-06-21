#import platforming_framework
import sys
# sys.path.append("./resources/code/")
import platforming_framework

#import pygame
import pygame
from pygame import *

pygame.init()

#configuration variables
WIDTH = 800
HEIGHT = 600
CAPTION = "Example Game"
PLAYER_SPEED = 5
FRAMES = 60

#boilerplate code
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
background = pygame.transform.scale(pygame.image.load("resources/images/bg.png"), (WIDTH, HEIGHT))

#entities
test_player = platforming_framework.Player(pygame.image.load("resources/images/sprite.png"), 0, HEIGHT)
test_platform = platforming_framework.Platform(pygame.Color(255,255,0), 500, 500, 200, 20)
test_goal = platforming_framework.Goal(pygame.Color(255, 20, 147), 650, 350, 20, 20)

def main():
    #runtime settings
    run = True
    clock = pygame.time.Clock()

    #runs every frame
    def refresh():
        #draw background
        window.blit(background, (0,0))
        #refresh entities
        test_player.refresh()
        test_platform.refresh()
        test_goal.refresh()
        #refresh screen
        pygame.display.flip()

    while run:
        #set FPS
        clock.tick(FRAMES)

        #exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        #player controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            test_player.go(-PLAYER_SPEED,0)
        if keys[pygame.K_RIGHT]:
            test_player.go(PLAYER_SPEED,0)
        if keys[pygame.K_SPACE]:
            test_player.reset()
        if keys[pygame.K_UP]:
            test_player.jump()
        if keys[pygame.K_DOWN]:
            test_player.go(0,PLAYER_SPEED)


        #refresh every frame
        refresh()

main()
