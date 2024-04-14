import pygame

from map import Scene
from player import Player

MAP_WIDTH = 30
MAP_HEIGHT = 20

TILE_SIZE = 64

WINDOW_WIDTH = TILE_SIZE*16
WINDOW_HEIGHT = TILE_SIZE*9

FPS = 60


# Functions


# Initialize pygame
pygame.init()


#build a pygame game loop
# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Clock for controlling the frame rate
clock = pygame.time.Clock()


scene_1 = Scene("map1.tmx")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic
    scene_1.handle_input()
    

    # Render graphics
    scene_1.render(window)

    # Update the display
    pygame.display.update()

    clock.tick(FPS)

# Clean up
pygame.quit()