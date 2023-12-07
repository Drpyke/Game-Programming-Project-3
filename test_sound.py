#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pygame
import sys
from my_engine import Sound3D

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 4096)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
img = pygame.image.load("sound_source.png")
original_img = pygame.transform.scale(img, (250, 250))  # Store the original image for reference

sound_playing = False

listener_x = 400
listener_y = 300

# Create the Sound3D object outside the game loop
test_sound = Sound3D(400, 300, "dangan.wav")
sound_playing = False

running = True
move_up = False
move_down = False
move_left = False
move_right = False

img_width, img_height = original_img.get_size()
img_x = (WIDTH - img_width) // 2
img_y = (HEIGHT - img_height) // 2

min_img_width = 100  # Set a minimum width for the image
min_img_height = 100  # Set a minimum height for the image
max_img_width = 500  # Set a maximum width for the image
max_img_height = 500  # Set a maximum height for the image

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_DOWN:
                move_down = True
            elif event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
            elif event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
    
    # Move the listener continuously while the keys are held
    if move_up:
        listener_y -= 3
        img_width = int(img_width * 1.01)
        img_height = int(img_height * 1.01)
    elif move_down:
        listener_y += 3
        img_width = int(img_width * 0.99)
        img_height = int(img_height * 0.99)
    elif move_left:
        listener_x -= 3
        img_x += 3  # Move the image to the right when moving left
    elif move_right:
        listener_x += 3
        img_x -= 3  # Move the image to the left when moving right

    # Apply maximum image size limits based on the sound volume
    max_scale = test_sound.get_sound_volume() * 400  # Adjust multiplier as needed
    img_width = min(img_width, max_scale)
    img_height = min(img_height, max_scale)

    # Apply minimum image size limits
    min_scale = test_sound.get_sound_volume() * 100  # Adjust multiplier as needed
    img_width = max(img_width, min_img_width)
    img_height = max(img_height, min_img_height)

    img = pygame.transform.scale(original_img, (img_width, img_height))
    
    test_sound.update_volume(listener_x, listener_y)

    screen.blit(img, (img_x, img_y))
    
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
sys.exit()


# In[ ]:





# In[ ]:





# In[ ]:




