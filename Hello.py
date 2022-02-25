import pygame
from sys import exit

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Time pass game")

clock = pygame.time.Clock()
screen.fill("Black")
player_surface = pygame.image.load('graphics/Player/player_walk_1.png')
player_rect  = player_surface.get_rect(midbottom=(400,400))
player_vel =6
player_gravity=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    keys =pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_rect.x+=player_vel
    if keys[pygame.K_SPACE]:
        print(keys[pygame.K_SPACE])
        player_gravity=-20    

        


    player_gravity+=2
    player_rect.y-=player_gravity
    
    screen.blit(player_surface,player_rect)
    
    clock.tick(60)
    pygame.display.update()
    