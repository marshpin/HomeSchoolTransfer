import sys
import pygame
import player
import colorama
import gameObjectClasses
from sys import exit as sysexit
from pygame import QUIT, quit as pyquit
from player import Player
from colorama import init as colorinit
from gameObjectClasses import Rectangle
colorinit()

gameLoop = True

screenSize = (400,400)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pygame home Project")

clock = pygame.time.Clock()

player = Player(16,16,(255,255,255))

while gameLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            pyquit()
            sysexit()
    screen.fill((0,0,0))
    rect1 = Rectangle(100,150,64,64,(255,0,0), "background", "rect1")
    player.update(screen)
    pygame.display.update()
    clock.tick(60)
