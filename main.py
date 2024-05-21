import pygame

from map import Scene
from map import BabyScene
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


#scene_1 = BabyScene("actual_map_stp_marche.tmx")
#scene_1 = Scene("map_destroyed_stp_marche.tmx")
#scene_1 = TroyennesScene("actual_map_stp_marche.tmx")
#scene_1 = Scene("C:\Users\bened\OneDrive\Dokumente\Studium\MA2\SHS\Game_maps\map_final_final_final.tmx")
scene_1 = Scene("map_final_final.tmx")


# Game loop
running = True
while running:
    scene_1 = scene_1.check_update_scene()
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