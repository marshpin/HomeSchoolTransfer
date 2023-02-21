import pygame
import colorama
import sys
from colorama import Fore
from sys import exit as sysexit

layers = ["background", "ground", "gfx"]


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
        if not layer in layers:
            ErrorMessage(f"Layer type of {self.objname} is unrecognizable! Unrecognized layer: {layer}", True)
        else:
            self.layer = layer
class GameObjectHandler():
    def __init__(self):
        self.GameObjects = []