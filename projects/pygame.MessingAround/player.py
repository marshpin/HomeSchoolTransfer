import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
    def update(self,screen):

        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen,self.color,self.rect)