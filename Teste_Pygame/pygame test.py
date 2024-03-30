import pygame, sys 
pygame.init()

screen = pygame.display.set_mode(size=(500,500))
clock = pygame.time.Clock()

mouse_pos = (0,0)
radius = 30
pygame.mouse.set_visible(False)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
            
        if(event.type == pygame.MOUSEWHEEL):
            if(event.y == 1):
                radius += 10
            else:
                radius -= 10
            
    mouse_pos = pygame.mouse.get_pos()
            
    screen.fill((0,0,0))
    box = pygame.draw.circle(screen, color=(255,255,255), center= mouse_pos, radius= radius)
    pygame.display.update()