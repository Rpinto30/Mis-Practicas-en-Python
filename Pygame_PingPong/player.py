import pygame
from Color import *

class new_player():
    def __init__(self, surface, player_pos = [], color_player = white, player_scale = [10,10], velocity = 0):
        self.surface = surface
        self.color_player = color_player
        self.velocity = velocity

        #POSITION
        self.player_pos_x = player_pos[0]
        self.player_pos_y = player_pos[1]

        #SCALE
        self.player_width = player_scale[0]
        self.player_height = player_scale[1]
    
    def player_draw(self, coords = [0,0]):
        pygame.draw.rect(surface= self.surface, color= self.color_player, 
                       rect= [coords[0], coords[1], self.player_width, self.player_height])

    def player_move(self, event, max_speed = 4, keys = [], coord = 0):
        if event.type == pygame.KEYDOWN:
            if event.key == keys[0]: self.velocity = max_speed
            if event.key == keys[1]: self.velocity = -max_speed

        if event.type == pygame.KEYUP:
            if event.key == keys[0]: self.velocity = 0
            if event.key == keys[1]: self.velocity = 0