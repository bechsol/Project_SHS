import pygame

from map import Scene
from player import Perso

MAP_WIDTH = 70
MAP_HEIGHT = 50

TILE_SIZE = 64

WINDOW_WIDTH = TILE_SIZE*16
WINDOW_HEIGHT = TILE_SIZE*9

FPS = 60

# Initialize pygame
pygame.init()


#build a pygame game loop
# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Clock for controlling the frame rate
clock = pygame.time.Clock()


scene_1 = Scene("map1.tmx")
#scene_2 = Scene("map_destroyed.tmx")

# Game loop
running = True
while running:

    # Update game logic
    running = scene_1.handle_input()
#    running = scene_2.handle_input()

    # Render graphics
    scene_1.render(window)
#    scene_2.render(window)
    # Update the display
    pygame.display.update()

    clock.tick(FPS)

# Clean up
pygame.quit()