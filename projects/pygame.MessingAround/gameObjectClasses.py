import pygame
import colorama
import sys
from colorama import Fore
from sys import exit as sysexit


layers = ["background", "ground", "gfx"]

gameObjects = {}

def ErrorMessage(msg, quit):
    print(Fore.RED + "ERROR: " + msg)
    if quit:
        sysexit()

class Rectangle(pygame.Rect):
    def __init__(self, x, y, width, height, color, layer, objname):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.objname = objname
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        if not layer in layers:
            ErrorMessage(f"Layer type of {self.objname} is unrecognizable! Unrecognized layer: {layer}", True)
        else:
            self.layer = layer
        gameObjects[self.layer].append((self.objname, (self.rect.x,self.rect.y,self.rect.width,self.rect.height), self.color))
class GameObjectHandler():
    def __init__(self):
        self.GameObjects = gameObjects
        for layer in layers:
            gameObjects[layer] = []
    def update(self, screen):
        self.GameObjects = gameObjects
        for layer in self.GameObjects:
            for obj in self.GameObjects[layer]:
                rect = obj[1]
                color = obj[2] 
                pygame.draw.rect(screen, color, rect)