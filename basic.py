from cgitb import text
import pygame
from sys import exit
from random import randint

pygame.init()

def display_score(screen):
    current_time=int(pygame.time.get_ticks()//1000-start_time//1000)
    score_surf = test_font.render(f"Score:{current_time}",False,(64,64,64))
    score_rect = score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    return current_time
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf",50)
sky_surface=pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if obstacle_rect.colliderect(player_rect):
                return [],False

            if obstacle_rect.colliderect(player_rect):
                game_active=False
            if obstacle_rect.x-5 <-100:
                obstacle_list.remove(obstacle_rect)
            obstacle_rect.x-= 5

            if obstacle_rect.bottom==300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)    
        return obstacle_list,True
    else:return [],True
# score_surface = test_font.render("My game",False,(64,64,64))
# score_rect  = score_surface.get_rect(midbottom=(400,50))
game_name = test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600,300))
snail_x_pos = 600

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,300))
fly_surface = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_rect = fly_surface.get_rect()
player_gravity = 0
game_active=False
start_time = 0
player_stand = pygame.image.load("graphics/Player/player_stand.png")
player_stand =pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400,200))
pixel_runner_surface = test_font.render("Pixel Runner",False,(111,196,169))
pixel_runner_rect = pixel_runner_surface.get_rect(center=(400,100))
score = 0
obstacle_timer = pygame.USEREVENT+1
pygame.time.set_timer(obstacle_timer,1600)


# obstacle 
obstacle_rect_list = []
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
        if event.type == obstacle_timer and game_active==True:
            
            if randint(0,2):
                obstacle_rect_list.append(snail_surface.get_rect(midbottom=(randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(bottomright=(randint(900,1100),210)))        

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        score = display_score(screen)

        screen.blit(player_surface,player_rect)
        player_gravity+=1
        player_rect.y+=player_gravity
        if player_rect.bottom >=300:
            player_rect.bottom=300

        if player_rect.colliderect(snail_rect):
            game_active=False

        obstacle_rect_list,game_active=obstacle_movement(obstacle_rect_list)    
        
    else:
        player_rect.bottom=300
        player_gravity=0
        screen.fill((94,129,162))
		# screen.blit(player_stand,player_stand_rect)
        screen.blit(player_stand,player_stand_rect)
        screen.blit(pixel_runner_surface,pixel_runner_rect)
        score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center =(550,40))
        screen.blit(score_message,score_message_rect)
        message_surface = test_font.render("Press Space to restart the game",False,(111,196,169))
        message_surface_rect = message_surface.get_rect(center =(400,350))
        screen.blit(message_surface,message_surface_rect)
		


    pygame.display.update()
    clock.tick(60)

