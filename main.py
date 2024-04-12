import pygame

from map import Map
from player import Player

MAP_WIDTH = 30
MAP_HEIGHT = 20

TILE_SIZE = 64

WINDOW_WIDTH = TILE_SIZE*16
WINDOW_HEIGHT = TILE_SIZE*9

FPS = 60


# Functions

def handle_input(player, map_tiles):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move_up(map_tiles)
    if keys[pygame.K_DOWN]:
        player.move_down(map_tiles)
    if keys[pygame.K_LEFT]:
        player.move_left(map_tiles)
    if keys[pygame.K_RIGHT]:
        player.move_right(map_tiles)


# Initialize pygame


pygame.init()


#build a pygame game loop
# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Clock for controlling the frame rate
clock = pygame.time.Clock()


map1 = Map(30, 20)
map1.load_tmx("map_test.tmx")
print(map1.tiles)

player = Player(WINDOW_WIDTH, WINDOW_HEIGHT)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic
    handle_input(player, map1.tiles)

    # Render graphics
    map1.render(window, (player.x - WINDOW_WIDTH//2, player.y - WINDOW_HEIGHT//2))
    player.render(window)

    # Update the display
    pygame.display.update()

    clock.tick(FPS)

# Clean up
pygame.quit()