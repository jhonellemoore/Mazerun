#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:23:15 2020
@author: Jhonelle, Lael, Kelsey, and Terry
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:06:11 2020
Template for project
"""

import pygame, sys, random
from pygame.locals import *
import time
from config import *

PLAYER_COLOUR = (0, 255, 0)
WALL_COLOUR = (0, 100, 0)
ENEMY_COLOUR = (255, 0, 0)
GRID_COLOR = (150, 75, 0)
BACKGROUND_COLOR = (150, 75, 0)
WHITE = (255, 255, 255)

COUNTDOWN_TIME = 60000
FRAMES_PER_SECOND = 60

GAME_CAPTION = "MAZE RUN"

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 768

# Tile config
TILE_SIZE = 32
GRID_WIDTH = DISPLAY_WIDTH / TILE_SIZE
GRID_HEIGHT = DISPLAY_HEIGHT / TILE_SIZE

LEFT_RIGHT = 0
UP_DOWN = 1

image_right = pygame.image.load("womanGreen_stand.png")
image_right.set_colorkey((255, 255,255))
image_right = pygame.transform.scale(image_right, (TILE_SIZE, TILE_SIZE)) #This is how you scale an image 
image_left = pygame.transform.flip(image_right, True, False)
image_up = pygame.transform.rotate(image_right, 90)
image_down = pygame.transform.rotate(image_right, -90)

zombie_right = pygame.image.load("zoimbie1_stand.png")
zombie_right.set_colorkey((255, 255,255))
zombie_right = pygame.transform.scale(zombie_right, (TILE_SIZE, TILE_SIZE)) #This is how you scale an image 
zombie_left = pygame.transform.flip(zombie_right, True, False)
zombie_up = pygame.transform.rotate(zombie_right, 90)
zombie_down = pygame.transform.rotate(zombie_right, -90)

lives_image = pygame.image.load("heart_shield.png")
lives_image = pygame.transform.scale(lives_image, (TILE_SIZE, TILE_SIZE))

font_name = pygame.font.match_font('arial')
   
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, walls):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.walls = walls
        self.lives = 3

              
    def move(self, x, y):
        self.rect.x += x * TILE_SIZE
        self.rect.y += y * TILE_SIZE
        
        if self.is_collided():
            self.rect.x -= x * TILE_SIZE
            self.rect.y -= y * TILE_SIZE
        
        if x > 0:
            self.image = image_right
        elif x < 0:
            self.image = image_left
        elif y > 0:
            self.image = image_down
        elif y < 0:
            self.image = image_up
    
    def is_collided(self):
        for wall in self.walls:
            if self.rect.colliderect(wall.get_rect()):
                return True
        return False
        
    
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type, walls):
        pygame.sprite.Sprite.__init__(self)
        self.image = zombie_right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.orientation = LEFT_RIGHT if enemy_type == 'H' else UP_DOWN
        self.walls = walls
        self.velocity = random.choice([-6, -5, -4, -3, 3, 4, 5, 6])

    def set_walls(self, walls):
        self.walls = walls

    def update(self):
        if self.orientation == LEFT_RIGHT:
            if self.velocity > 0:
                self.image = zombie_right
            else:
                self.image = zombie_left
            self.rect.x += self.velocity
        else:
            if self.velocity > 0:
                self.image = zombie_down
            else:
                self.image = zombie_up
            self.rect.y += self.velocity


        collisions = pygame.sprite.spritecollide(self, self.walls, False)
            
        if collisions: 
            if self.orientation == LEFT_RIGHT:
                self.rect.x -= self.velocity
            else:
                self.rect.y -= self.velocity                
        
            self.velocity = -self.velocity  
    
    def is_collided(self):
        for wall in self.walls:
            if self.rect.colliderect(wall.get_rect()):
                return True
        return False


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tile_99.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        pass
        
    def get_rect(self):
        return self.rect


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    
def get_game_elements():
    map_list = random.choice(WALL_MAP)
    map_elements = map_list.split('\n')
    
    start_x, start_y = 0, 0
    player = None
    enemies = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    all_sprites_group = pygame.sprite.Group()
    
    for row in map_elements:
        for column in row:
            if column == 'W':
                wall = Wall(start_x, start_y)
                walls.add(wall)
                all_sprites_group.add(wall)
            elif column == 'H' or column == 'V':
                enemy = Enemy(start_x, start_y, column, walls)
                enemies.add(enemy)
                all_sprites_group.add(enemy)
            elif column == 'P':
                player = Player(start_x, start_y, walls)
                all_sprites_group.add(player)
            start_x += TILE_SIZE
        start_x = 0
        start_y += TILE_SIZE
        
    return enemies, walls, player, all_sprites_group



def events(player):
    for event in pygame.event.get(): # Get system events
            if event.type == pygame.QUIT: # Exit game loop if window closed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move(1, 0)
                if event.key == pygame.K_LEFT:
                    player.move(-1, 0)
                if event.key == pygame.K_UP:
                    player.move(0, -1)
                if event.key == pygame.K_DOWN:
                    player.move(0, 1)
                    
                

def update(elements):
    elements.update()


def restart(display_surface):
    display_surface.fill(BACKGROUND_COLOR)
    draw_text(display_surface, 'Press Spacebar to try again! (Press Q to exit)', 45, DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return 
                
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()
    
def game_over(display_surface):
    draw_text(display_surface, 'Game Over!' , 45, DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2)
    pygame.display.update()
    pygame.time.wait(2000)

def you_win(display_surface):
    draw_text(display_surface, 'You Win!' , 45, DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2)
    pygame.display.update()
    pygame.time.wait(2000)

def show_lives(lives, display_surface, heart):
    x = 15
    for i in range(lives):
        display_surface.blit(heart, [x, 15])
        x += 35
    
def main():
    pygame.init()
    pygame.mixer.init()
    display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption(GAME_CAPTION)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(200, 100)
    pygame.mixer.music.load('Aunt_Tagonist_Silent_Film_Dark.mp3')
    pygame.mixer.music.play(loops = -1)
        
    enemies, walls, player, all_sprites = get_game_elements()
    start_time = pygame.time.get_ticks()
    i_timer = 0
    #invincible = False
    player_start_x = player.rect.x
    player_start_y = player.rect.y
 

    game_start = False
    start_screen = pygame.image.load('newstartscreen.png')
    start_screen = pygame.transform.scale(start_screen, (DISPLAY_WIDTH, DISPLAY_HEIGHT))


    while game_start == False:
        keys = pygame.key.get_pressed()
        display_surface.blit(start_screen, [0,0])
        for event in pygame.event.get():
            if event.type == QUIT or keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not keys[K_ESCAPE]:
                game_start = True
        pygame.display.update()
    
    while game_start:
        
        display_surface.fill(BACKGROUND_COLOR)
        current_time = pygame.time.get_ticks()
        printed_time = current_time - start_time
        if printed_time >= COUNTDOWN_TIME:
            game_over(display_surface)
            restart(display_surface)
            enemies, walls, player, all_sprites = get_game_elements()
            start_time = pygame.time.get_ticks()


        clock.tick(FRAMES_PER_SECOND) # Keeps the loop runnin at the right rate

        enemy_collide = pygame.sprite.spritecollide(player, enemies, False)
        if enemy_collide:
                player.lives-= 1
                player.rect.x = player_start_x
                player.rect.y = player_start_y

                
                if player.lives == 0:
                    game_over(display_surface)
                    restart(display_surface)
                    enemies, walls, player, all_sprites = get_game_elements()
                    start_time = pygame.time.get_ticks()

    

        if (player.rect.x < 0 or player.rect.x >= DISPLAY_WIDTH or player.rect.y < 0 or player.rect.y >= DISPLAY_HEIGHT):
            you_win(display_surface)
            restart(display_surface)
            enemies, walls, player, all_sprites = get_game_elements()
            start_time = pygame.time.get_ticks()

        events(player)
        update(all_sprites)
        all_sprites.draw(display_surface)
        draw_text(display_surface, str(COUNTDOWN_TIME//1000 - (printed_time//1000)), 24, int(DISPLAY_WIDTH*0.92), int(DISPLAY_HEIGHT*0.01))
        show_lives(player.lives, display_surface, lives_image)        
        pygame.display.update() # Update the display


if __name__ == "__main__":
    main()
