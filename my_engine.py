import pygame
import numpy as np
import math

class Physics:
    
    acc_gravity = 0.5
    f_coef = 0.1
    
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_x = 0
        self.velocity_y = 0
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def update(self, acc_gravity, screen_width, screen_height, f_coef):
        self.velocity_y += self.acc_gravity
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Collision with the ground (bottom of the screen)
        if self.y + self.radius >= screen_height:
            self.y = screen_height - self.radius
            self.velocity_y = -self.velocity_y * 0.6  # Reduced energy after bouncing
        
        # Collision with the right wall
        if self.x + self.radius >= screen_width:
            self.x = screen_width - self.radius
            self.velocity_x = -self.velocity_x  # Reverse x-velocity when hitting the right wall
        
        # Collision with the left wall
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.velocity_x = -self.velocity_x  # Reverse x-velocity when hitting the left wall
        
        # Friction application
        if self.velocity_x != 0:
            friction_force = -1 * self.f_coef * (self.velocity_x / abs(self.velocity_x))
            self.velocity_x += friction_force
    
    def apply_force(self, force_x, force_y):
        self.velocity_x += force_x
        self.velocity_y += force_y
    
    def collision_detection(self, a_object):
        distance = math.sqrt((self.x - a_object.x) ** 2 + (self.y - a_object.y) ** 2)
        if distance <= self.radius + a_object.radius:
            return True
        return False
    
    def handle_collision(self, a_object):
        if self.collision_detection(a_object):
            distance_x = a_object.x - self.x
            distance_y = a_object.y - self.y
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

            overlap = self.radius + a_object.radius - distance
            if overlap > 0:
                direction_x = distance_x / distance
                direction_y = distance_y / distance

                self.x -= overlap / 2 * direction_x
                self.y -= overlap / 2 * direction_y
                a_object.x += overlap / 2 * direction_x
                a_object.y += overlap / 2 * direction_y

                self.velocity_x -= overlap / 2 * direction_x
                self.velocity_y -= overlap / 2 * direction_y
                a_object.velocity_x += overlap / 2 * direction_x
                a_object.velocity_y += overlap / 2 * direction_y
    
    
    def jump_force(self, force):
        self.velocity_y += force

class Sound3D:
      
    def __init__(self, lis_x, lis_y, filename):
        self.x = lis_x
        self.y = lis_y
        self.sound = pygame.mixer.Sound(filename)
        self.default_volume = 0.5  # Adjust this to your desired default volume
        self.channel = self.sound_play()  # Play the sound once and store the channel
    
    def sound_play(self):
        channel = self.sound.play(-1)
        return channel
    
    def get_sound_volume(self):
        return self.sound.get_volume()
    
    def update_volume(self, lis_x, lis_y):
        max_vol = 1.0
        min_vol = 0.0
        
        # Calculate the distance between the listener and sound source
        distance_y = lis_y - self.y
        distance_x = lis_x - self.x
        
        # Calculate the volume based on the distance from the center of the screen (y-coordinate)
        volume_y = self.default_volume - 0.004 * distance_y
        
        # Apply panning effect based on the distance from the center of the screen (x-coordinate)
        volume_L = volume_y
        volume_R = volume_y
        
        if distance_x < 0:
            volume_L += 0.003 * distance_x
            volume_R += 0.002 * distance_x
        elif distance_x > 0:
            volume_L -= 0.002 * distance_x
            volume_R -= 0.003 * distance_x
        
        # Clamp the volume within the valid range
        volume_L = max(min_vol, min(volume_L, max_vol))
        volume_R = max(min_vol, min(volume_R, max_vol))
        
        self.channel.set_volume(volume_L, volume_R)