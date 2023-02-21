import pygame
import colorama
from colorama import Fore

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.isGrounded = False
        self.velx = 0
        self.vely = 0
        self.velycrement = .050
    def update(self,screen, gameObjects):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            self.x += 1.5
        if pressed[pygame.K_a]:
            self.x -= 1.5
        def groundCheck():
            for obj in gameObjects["ground"]:
                object = obj[1]
                rect = pygame.Rect(object[0], object[1], object[2], object[3])
                groundcheck = pygame.Rect(self.rect.x + 5,self.rect.y + 8 + 5,2,6)
                if groundcheck.colliderect(rect):
                    self.isGrounded = True
                    if self.isGrounded and self.y != rect.y - self.height:
                        self.y = rect.y - self.height
                    self.vely = 0
                    self.velycrement = 0
                elif self.isGrounded == True and not groundcheck.colliderect(rect):
                    self.isGrounded = False
            if not self.isGrounded:
                self.velycrement = .050
                self.vely += self.velycrement
                self.velycrement += .0012
            if self.vely > 5:
                self.velycrement = 0
            self.y += self.vely
        
                
        groundCheck()
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen,self.color,self.rect)