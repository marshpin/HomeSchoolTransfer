import pygame

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
        self.velycrement = .05
    def update(self,screen, gameObjects):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            self.x += 1
        if pressed[pygame.K_a]:
            self.x -= 1
        def groundCheck():
            if not self.isGrounded:
                self.vely += self.velycrement
                self.velycrement += .05
            self.y = self.vely
        print(gameObjects["ground"])
        #if self.rect.collidelist(gameObjects["ground"][1]):
            #print("aaa")
        groundCheck()
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen,self.color,self.rect)