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
        self.canGoRight = True
        self.canGoLeft = True
    def update(self,screen, gameObjects):
        def groundCheck():
            for obj in gameObjects["ground"]:
                object = obj[1]
                rect = pygame.Rect(object[0], object[1], object[2], object[3])
                if self.rect.colliderect(rect):
                    self.isGrounded = True
                    if self.y != rect.y - self.height and self.isGrounded:
                        self.y = rect.y - self.height
                    self.vely = 0
                    self.velycrement = 0
                if self.isGrounded:
                    pass
                #if self.isGrounded and not rect.top - self.rect.bottom <= 5 and rect.right / 1.1 - self.rect.left <= rect.width / 1.55:
                    #self.isGrounded = False
                #if rect.top - self.rect.bottom or self.rect.top - rect.bottom == 0:
                    #self.isGrounded = True
                    #if self.isGrounded and self.y != rect.y - self.height:
                        #self.y = rect.y - self.height
                    #self.vely = 0
                    #self.velycrement = 0
                #elif self.isGrounded == True and not rect.top - self.rect.bottom or self.rect.top - rect.bottom == 0:
                    #self.isGrounded = False
                #if pygame.Rect.collidepoint(rect, self.rect.right, self.rect.top):
                    #self.canGoRight = False
                #elif self.canGoRight == False and not pygame.Rect.collidepoint(rect, self.rect.right, self.rect.top):
                    #self.canGoRight = True
            if not self.isGrounded:
                self.velycrement = .050
                self.vely += self.velycrement
                self.velycrement += .0012
            if self.vely > 5:
                self.velycrement = 0
            self.y += self.vely
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d] and self.canGoRight:
            self.x += 1.5
        if pressed[pygame.K_a] and self.canGoLeft:
            self.x -= 1.5
    
        groundCheck()
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen,self.color,self.rect)