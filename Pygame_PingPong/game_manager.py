import pygame, sys
from player import *
from ball import *
game_run = True

width = 400
height = 600
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([width, height])

#PLAYER DATA (GENERAL)
player_scale = 50
player_margen = 20

#PLAYER_1
player1_velocity = 0

coord_x_player1 = (width/2) - (player_scale/2)
coord_y_player1 = height - (player_scale + player_margen)
coord_player1 = [coord_x_player1, coord_y_player1]

p1 = new_player(surface= screen, player_pos= coord_player1, color_player= red, 
                player_scale=[player_scale, player_scale])

#PLAYER_2
player2_velocity = 0

coord_x_player2 = (width/2) - (player_scale/2)
coord_y_player2 = player_margen
coord_player2 = [coord_x_player2, coord_y_player2]

p2 = new_player(surface= screen, player_pos=coord_player2, color_player= green, 
                player_scale=[player_scale, player_scale])

#BALL
ball_scale = 25
ball_speed_x = 0
ball_speed_y = 0
velocity_ball = [ball_speed_x, ball_speed_y]

coord_x_ball = width/2 - (ball_scale/2)
coord_y_ball = height/2 - (ball_scale/2)
coord_ball = [coord_x_ball, coord_y_ball]

ball = ball_game(surface= screen, position= coord_ball, scale= [ball_scale, ball_scale])

def system_move(limit = [0,1]):
        global coord_x_player1
        global coord_x_player2
        
        #ARREGLAR PORFAVOOOOOOOOOOOOOR
        if(coord_x_player1 >= limit[0] and coord_x_player1 <= limit[1]): coord_x_player1 += player1_velocity
        if(coord_x_player1 <= 0): coord_x_player1 = 0
        if(coord_x_player1 >= width - (player_scale)): coord_x_player1 = width - (player_scale)

        if(coord_x_player2 >= limit[0] and coord_x_player2 <= limit[1]): coord_x_player2 += player2_velocity
        if(coord_x_player2 <= 0): coord_x_player2 = 0
        if(coord_x_player2 >= width - (player_scale)): coord_x_player2 = width - (player_scale)
        

def system_move_ball():
    global coord_x_ball
    global coord_y_ball

    coord_x_ball += velocity_ball[0]
    coord_y_ball += velocity_ball[1]

def check_collider():
        pass

while game_run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            game_run = False
        
        #MOVE
        #PLAYER 1
        p1.player_move(event=event, keys= [pygame.K_d, pygame.K_a], coord= coord_x_player1)
        player1_velocity = p1.velocity 
        #PLAYER 2
        p2.player_move(event=event, keys= [pygame.K_RIGHT, pygame.K_LEFT], coord= coord_x_player2)
        player2_velocity = p2.velocity

    check_collider()

    ball.ball_move(coords= [coord_x_ball, coord_y_ball], 
                       limit=[width - ball_scale, height - ball_scale])
    velocity_ball[0] = ball.velocity[0]
    velocity_ball[1] = ball.velocity[1]

    screen.fill(black)

    system_move(limit= [0, width])
    system_move_ball()

    sprite_p1 = p1.player_draw(coords=[coord_x_player1, coord_y_player1])
    sprite_p2 =p2.player_draw(coords=[coord_x_player2, coord_y_player2])
    sprite_ball = ball.ball_draw(coords= [coord_x_ball, coord_y_ball])

    clock.tick(60)
    pygame.display.flip()

sys.exit()