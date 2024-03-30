import pygame
from Color import *

class ball_game():
    def __init__(self, surface, position = [], color = white, scale = [5,5], 
                 velocity = [0,0], max_speed = [1,1]):
        self.surface = surface
        self.position = position
        self.color = color

        self.scale = scale
        self.width = scale[0]
        self.height = scale[1]

        self.velocity = velocity
        self.max_speed = max_speed

    def ball_draw(self, coords = [0,0]):
        pygame.draw.rect(surface= self.surface, color= self.color, 
                       rect= [coords[0], coords[1], self.width, self.height])


    def ball_move(self, coords = [0,0], limit = [0,0]):
        if(coords[0] > limit[0] or coords[0] < 0): 
            self.max_speed[0] *= -1 

        if(coords[1] > limit[1] or coords[1] < 0): 
            self.max_speed[1] *= -1 

        self.velocity[0] = self.max_speed[0]
        self.velocity[1] = self.max_speed[1]

        