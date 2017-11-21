import pygame
import math
from pygame.locals import *
import random
import datetime

winwith = 1920
winheight = 1080
centerx = winwith / 2
centery = winheight / 2
screen = pygame.display.set_mode((winwith, winheight), FULLSCREEN | DOUBLEBUF)
screen.fill((0, 0, 0))
pygame.mouse.set_visible(False)
pygame.display.update()
running = True
prnt = False


class Spiral:
    def __init__(self, n, c, grad, seed, colors):
        self.n = n
        self.c = c
        self.grad = grad
        self.x = 1
        self.y = 1
        self.seed = seed
        self.r = 0
        self.rdir = 1
        self.colors = colors

    def Draw(self):
        a = self.n * self.grad
        r = self.c * math.sqrt(self.n)
        self.x = int((r * math.cos(a)) + centerx)
        self.y = int((r * math.sin(a)) + centery)
        if self.seed == 1 or self.seed == 3 or self.seed == 7:
            pygame.draw.circle(screen, (self.r, self.r, 255), (self.x, self.y), 10, 3)
        if self.seed == 1 or self.seed == 2 or self.seed == 8:
            pygame.draw.circle(screen, (255, self.r, self.r), (self.x, self.y), 3, 0)
        if self.seed == 4 or self.seed == 6 or self.seed == 8:
            pygame.draw.circle(screen, (self.r, 255, 255-self.r), (self.x, self.y), 10, 3)
        if self.seed == 4 or self.seed == 5 or self.seed == 7:
            pygame.draw.circle(screen, (255, 255-self.r, 255), (self.x, self.y), 3, 0)

        self.n += 1
        self.r += self.rdir
        if self.r > 254 or self.r < 1:
            if self.colors == 1: self.rdir = -self.rdir
            if self.colors == 2: self.r = 255 - self.r
        pygame.display.flip()


m = Spiral(0, 7, 137.508, random.randint(1, 8), random.randint(1, 2))

while running:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        running = False
    if pressed[pygame.K_SPACE]:
        m = Spiral(0, random.randint(1, 20), random.randint(100, 50000)/99, random.randint(1, 8), random.randint(1, 2))
        screen.fill((0, 0, 0))
    if pressed[pygame.K_p]:
        prnt = True
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    if m.x > winwith + 150:
        if prnt == True:
            stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            pygame.image.save(screen, "screenshot" + stamp + ".jpeg")
            prnt = False
        m = Spiral(0, random.randint(1, 20), random.randint(100, 50000)/99, random.randint(1, 8), random.randint(1, 2))
        screen.fill((0, 0, 0))

    m.Draw()
