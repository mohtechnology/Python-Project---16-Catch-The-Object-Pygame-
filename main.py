import pygame
import random

pygame.init()

width, height = 400, 600
win = pygame.display.set_mode((width, height))

# Player Properties
player_width = 100
player_height = 20
player_x = 150
player_y = 570
player_speed = 10

# obj Properties
obj_width = 30
obj_height = 30
obj_x = random.randint(10, 370)
obj_y = 0
obj_speed = 10

# Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

font = pygame.font.SysFont('comicsans', 30)
pygame.display.set_caption("Catch The Object")

score = 0
attempts = 3
running = True
while running and attempts > 0:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    obj_y += obj_speed
    if obj_y > 600:
        obj_y = 0
        attempts -= 1
        obj_x = random.randint(10, 370)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 10:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 290:
        player_x += player_speed

    if (obj_y + obj_height > player_y and obj_x + obj_width > player_x and obj_x < player_x + player_width):
        score += 1
        obj_y = 0
        obj_x = random.randint(10, 370)
    
    win.fill(black)

    pygame.draw.rect(win, red, (obj_x, obj_y, obj_width, obj_height))
    pygame.draw.rect(win, white, (player_x, player_y, player_width, player_height))
    score_text = font.render(f"Score : {score}", 1, white)
    attempts_text = font.render(f"Attempts : {attempts}", 1, white)

    win.blit(score_text, (10,10))
    win.blit(attempts_text,(10, 40))

    pygame.display.update()
