from cgitb import text
import pygame
from sys import exit

pygame.init()

def display_score(screen):
    current_time=int(pygame.time.get_ticks()//1000-start_time//1000)
    score_surf = test_font.render(f"Score:ss{current_time}",False,(64,64,64))
    score_rect = score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    # print(current_time)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf",50)
sky_surface=pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()

# score_surface = test_font.render("My game",False,(64,64,64))
# score_rect  = score_surface.get_rect(midbottom=(400,50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600,300))
snail_x_pos = 600

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,300))
player_gravity = 0
game_active=True
start_time = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity =-20  
        elif game_active==False:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_time =pygame.time.get_ticks()
                game_active=True
                snail_rect.left=800
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10 )
        # screen.blit(score_surface,score_rect)
        display_score(screen)
        snail_rect.x -=5
        if snail_rect.right <0:
            snail_rect.left=800
        screen.blit(snail_surface,snail_rect)
        screen.blit(player_surface,player_rect)
        player_gravity+=1
        player_rect.y+=player_gravity
        if player_rect.bottom >=300:
            player_rect.bottom=300

        if player_rect.colliderect(snail_rect):
            game_active=False
    else:
        screen.fill("Red")    
    pygame.display.update()
    clock.tick(60)


    # 1:48