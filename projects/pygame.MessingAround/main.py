import sys
import pygame
import player
import colorama
import gameObjectClasses
from sys import exit as sysexit
from pygame import QUIT, quit as pyquit
from player import Player
from colorama import init as colorinit
from gameObjectClasses import Rectangle, GameObjectHandler
colorinit()

gameLoop = True

screenSize = (400,400)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pygame home Project")

clock = pygame.time.Clock()

player = Player(16,16,(255,255,255))
ObjectHandler = GameObjectHandler()

Rectangle(0,0,screenSize[0], screenSize[1], (12,12,12), "background", "backgroundblock")
Rectangle(50,50,28,28,(0,0,255), "background", "rect1")
Rectangle(128,128,32,32,(255,0,255), "background", "rect2")
Rectangle(200,200,16,16,(255,0,0), "ground", "rect3")
Rectangle(100,150,64,64,(0,255,0), "ground", "rect4")
Rectangle(0, screenSize[1] - 70, screenSize[0], 70, (24,24,24), "ground", "groundblock")

while gameLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            pyquit()
            sysexit()
    ObjectHandler.update(screen)
    player.update(screen, ObjectHandler.GameObjects)
    pygame.display.update()
    clock.tick(60)
