#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import sys
from my_engine import Physics

WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.98
FRICTION = 0.1
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (238, 130, 238)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

balls = [
    Physics(100, 100, 40, RED),
    Physics(200, 300, 50, BLUE),
    Physics(400, 200, 35, GREEN),
    Physics(300, 400, 45, ORANGE),
    Physics(500, 100, 40, YELLOW),
    Physics(600, 300, 50, INDIGO),
    Physics(700, 200, 35, VIOLET),
    Physics(250, 500, 45, RED),
    Physics(450, 150, 40, BLUE),
    Physics(550, 350, 50, GREEN),
    Physics(100, 400, 35, ORANGE),
    Physics(300, 200, 45, YELLOW),
    Physics(500, 500, 40, INDIGO),
    Physics(700, 150, 50, VIOLET),
    Physics(250, 300, 35, RED),
    Physics(450, 400, 40, BLUE),
    Physics(150, 350, 50, GREEN),
    Physics(650, 300, 35, ORANGE),
    Physics(300, 500, 45, YELLOW),
    Physics(600, 150, 40, INDIGO)
]

for ball in balls:
    ball.velocity_x = 3

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        for ball in balls:
            ball.apply_force(1, -7)  # Apply an upward force when spacebar is pressed

    for ball in balls:
        ball.update(GRAVITY, WIDTH, HEIGHT, FRICTION)

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].handle_collision(balls[j])

    for ball in balls:
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()


# In[ ]:





# In[ ]:




