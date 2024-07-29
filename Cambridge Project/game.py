import pygame
import os
import sys
import math 
from pygame.locals import *
import numpy as np
from pygame import mixer

pygame.display.set_caption('Cambridge Project')
img_path = os.path.join('player.png')
walkRight = [pygame.image.load('R1E.png')]
walkLeft = [pygame.image.load('L1E.png')]
pa = [pygame.image.load('pa.png')]
pa1 = [pygame.image.load('pa1.png')]

# ↓ Starting Music ( made it myself :) ) ↓
#mixer.init()
#mixer.music.load('Cmaj7Bmin7.wav')
#mixer.music.play()

pygame.init()

vec = pygame.math.Vector2
HEIGHT = 600
WIDTH = 800
ACC = 0.001
FRIC = 0.0005
FPS = 40
pos = 0
ace = 0
FramePerSec = pygame.time.Clock()
worldy = 240
ty = 50
pnt = 0
pnt_increment = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
bg = pygame.image.load("bg.png")
a = 'VCR.ttf'


class enemy(object):
    walkRight = [pygame.image.load('R1E.png')]
    walkLeft = [pygame.image.load('L1E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end] 
        self.walkCount = 0
        self.vel = 1
        self.r = 30

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33: 
                                     
            self.walkCount = 0
        
        if self.vel > 0: 
            win.blit(self.walkRight[0], (self.x,self.y))
            self.walkCount += 1
        else:  
            win.blit(self.walkLeft[0], (self.x,self.y))
            self.walkCount += 1    
    
    def move(self):
        if self.vel > 0:  
            if self.x < self.path[1] + self.vel: 
                self.x += self.vel
            else: 
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else: 
            if self.x > self.path[0] - self.vel: 
                self.x += self.vel
            else:  
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
                

class bird(object):
    walkRight = [pygame.image.load('bird.png')]
    walkLeft = [pygame.image.load('bird2.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end] 
        self.walkCount = 0
        self.vel = 5
        self.r = 30

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33: 
                                     
            self.walkCount = 0
        
        if self.vel > 0: 
            win.blit(self.walkRight[0], (self.x,self.y))
            self.walkCount += 1
        else:  
            win.blit(self.walkLeft[0], (self.x,self.y))
            self.walkCount += 1    
    
    def move(self):
        if self.vel > 0:  
            if self.x < self.path[1] + self.vel: 
                self.x += self.vel
            else: 
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else: 
            if self.x > self.path[0] - self.vel: 
                self.x += self.vel
            else:  
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0


class point(object):
    walkRight = [pygame.image.load('pa.png')]
    walkLeft = [pygame.image.load('pa1.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end] 
        self.walkCount = 0
        self.vel = 0
        self.r = 25

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33: 
                                     
            self.walkCount = 0
        
        if self.vel > 0: 
            win.blit(self.walkRight[0], (self.x,self.y))
            self.walkCount += 1
        else:  
            win.blit(self.walkLeft[0], (self.x,self.y))
            self.walkCount += 1    
    
    def move(self):
        if self.vel > 0:  
            if self.x < self.path[1] + self.vel: 
                self.x += self.vel
            else: 
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else: 
            if self.x > self.path[0] - self.vel: 
                self.x += self.vel
            else:  
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0


class player(object): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path).convert_alpha()
        self.x = 0
        self.y = 250

        self.pos = vec((0,250))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.r = 20

    def move(self):

        pressed_keys = pygame.key.get_pressed()  
              
        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -ACC * 25
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = ACC * 25
        if pressed_keys[pygame.K_UP]:
            self.vel.y = -6
        
        tmp_pot_accc = self.acc.x - self.vel.x * FRIC
        if tmp_pot_accc * self.acc.x > 0:
            self.acc.x -= self.vel.x * FRIC
        else:
            self.acc.x = 0
        self.vel += self.acc 
        self.pos += self.vel

        if (self.pos.x > 300 and self.pos.x < 380) or (self.pos.x > 520 and self.pos.x < 560):
            self.acc.y = 1

        elif self.pos.y > 250:
            self.pos.y = 250

        if self.pos.y < 0:
            self.pos.y = 0

        if self.pos.y < 230:
            self.acc.y = 1

        if self.acc.y > 5:
            self.acc.y = 5

        if self.acc.y < -5:
            self.acc.y = -5

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.y > 400:
            sys.exit()
     
    def Colision(self,x,y,r):
        dist = math.sqrt((x-self.pos.x) **2 + (y-self.pos.y) **2)
        if dist < r + self.r:
            return True
        return False
    
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.pos.x,self.pos.y), self.radius)        


    def draw(self, surface):
        surface.blit(self.image, (self.pos.x, self.pos.y))
            
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))


player = player()
platform = platform()

goblin = enemy(100, 250, 64, 64, 245)
bird1 = bird(-100, 150, 48, 48, 900)

ran_1 = np.random.randint(low=50, high=750)
points = point(ran_1, 150, 48, 48, ran_1)   

clock = pygame.time.Clock()

font = pygame.font.Font(a, 35)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()

    
    player.move()

    if player.Colision(goblin.x, goblin.y, goblin.r):
        pygame.quit()

    if player.Colision(bird1.x, bird1.y, bird1.r):
        pygame.quit()

    if player.Colision(points.x, points.y, points.r):
        pnt += pnt_increment
        # ↓ Point Sound ↓
        #mixer.music.load('Point.wav')
        #mixer.music.play()
        #print("Points: ")
        #print(pnt) 
        ranx_2 = np.random.randint(low=50, high=750)
        rany_2 = np.random.randint(low=100, high=250)
        points = point(ranx_2, rany_2, 48, 48, ranx_2)  

    screen.fill((255,255,255)) 
    screen.blit(bg, (0,0))
    player.draw(screen)
    goblin.draw(screen)
    bird1.draw(screen)
    points.draw(screen)
    point_text = font.render(f'Points: {pnt}', True, (255, 239, 201))
    screen.blit(point_text, (10, 10))
    pygame.display.update() 
    clock.tick(60)
