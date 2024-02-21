import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

#Gives the caption of the widow
pygame.display.set_caption("Platformer")

#Global variables
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 60
#Velocity of the player in the game
PLAYER_VEL = 5
#Initializing the widow of our game
window = pygame.display.set_mode((WIDTH, HEIGHT))

#Player attributes
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_velocity = 0
        self.y_velocity = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, velocity):
        self.x_velocity = -velocity
        if self.direction != "left":  
            self.direction = "left"
            self.animation_count = 0  

    def move_right(self, velocity):   
        self.x_velocity = velocity
        if self.direction != "rigth":  
            self.direction = "right"
            self.animation_count = 0   
    
    def jump(self, velocity):
        self.y_velocity = velocity
        if self.direction != "Up": 
            self.direction = "Up"
            self.animation_count = 0 


    def loop(self, fps):
        self.move(self.x_velocity, self.y_velocity)
    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)

#Get the background of the game
def get_background(name):
    image = pygame.image.load(join("assets", "background", name))
    _, _, width, height = image.get_rect()
    tiles = []

#Tells me how many tiles I need in the X and Y directions
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

#Draws the background plus the sprites and terrain tiles
def draw(window, background, bg_image, player):

    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)

    pygame.display.update()

def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_velocity = 0
    if keys[pygame.K_a]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_d]:
        player.move_right(PLAYER_VEL)
    if keys[pygame.K_w]:
        player.jump(PLAYER_VEL)

#Function that runs the game
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    player = Player(100, 100, 50, 50)

    run = True
    while run:
#Clock will regulate the framerate across multiple devices
        clock.tick(FPS)

#This checks if the player exists the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)

    pygame.quit()
    quit()


#Only call main function if we call the main(window) function
if __name__ == "__main__":
    main(window)


