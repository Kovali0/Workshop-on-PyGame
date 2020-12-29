import sys
from time import sleep

import pygame
from pygame.locals import *
clock = pygame.time.Clock() # set up the clock
BG = pygame.image.load('background1.jpg')
WINDOW_SIZE = (BG.get_width(), BG.get_height())
PLAYER_START_LOCATION = [100, 275]
PLATFORMXY = [200, 200]

class Player():
    def __init__(self):
        super().__init__()
        self.location = PLAYER_START_LOCATION
        self.sideFocus = "left"
        self.walkR = [pygame.image.load('here_we_go/mario_walk_right1.png'), pygame.image.load('here_we_go/mario_walk_right2.png'), pygame.image.load('here_we_go/mario_walk_right3.png')]
        self.walkL = [pygame.image.load('here_we_go/mario_walk_left1.png'), pygame.image.load('here_we_go/mario_walk_left2.png'), pygame.image.load('here_we_go/mario_walk_left3.png')]
        self.currentPose = 0

def initGame():
    pygame.init()
    pygame.display.set_caption('Pygame Window')

def renderGameWindow():
    screen.blit(BG, (0, 0))  # This will draw our background image at (0,0)
    screen.blit(pygame.image.load('platform.png'), PLATFORMXY)
    if player.sideFocus == "left":
        screen.blit(player.walkL[player.currentPose], player.location)
    else:
        screen.blit(player.walkR[player.currentPose], player.location)
    pygame.display.update()

if __name__ == '__main__':
    initGame()
    screen = pygame.display.set_mode((1280, 720))
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    move_counter = 0
    jump = False
    on_ground = True
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if jump:
            player.location[1] -= 10
            jump = False
        else:
            if player.location[1] < 275:
                player.location[1] += 2

        if player.location[1] == 275:
            on_ground = True

        if pygame.key.get_pressed()[pygame.K_d]:
            player.location[0] += 4
            move_counter += 1
            player.sideFocus = "right"
            player.currentPose = move_counter%3

        if pygame.key.get_pressed()[pygame.K_a]:
            if player.location[0] is not 0:
                player.location[0] -= 4
                move_counter += 1
                player.sideFocus = "left"
                player.currentPose = move_counter%3

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if on_ground:
                player.location[1] -= 10
                jump = True
                on_ground = False

        renderGameWindow()
        clock.tick(60)