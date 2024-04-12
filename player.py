import pygame

MAP_WIDTH = 30
MAP_HEIGHT = 20

TILE_SIZE = 64

WINDOW_WIDTH = TILE_SIZE*16
WINDOW_HEIGHT = TILE_SIZE*9

class Player:
    def __init__(self, x, y, x_size=64, y_size=64):
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.speed = 3

    def render(self, window):
        # Calculate the position and size of the rectangle
        rect_width = self.x_size
        rect_height = self.y_size

        if self.x < WINDOW_WIDTH//2:
            rect_x = self.x - rect_width//2
        elif self.x > MAP_WIDTH*TILE_SIZE - WINDOW_WIDTH//2:
            rect_x = WINDOW_WIDTH + self.x - MAP_WIDTH*TILE_SIZE - rect_width//2
        else:
            rect_x = (WINDOW_WIDTH - rect_width) // 2

        if self.y < WINDOW_HEIGHT//2:
            rect_y = self.y - rect_height//2
        elif self.y > MAP_HEIGHT*TILE_SIZE - WINDOW_HEIGHT//2:
            rect_y = WINDOW_HEIGHT + self.y - MAP_HEIGHT*TILE_SIZE - rect_height//2
        else:
            rect_y = (WINDOW_HEIGHT - rect_height) // 2

        # Draw the rectangle on the screen
        pygame.draw.rect(window, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))

    def move_up(self, map_tiles):
        for row in map_tiles:
            for tile in row:
                if tile is not None:
                    if (self.x > tile.x - self.x_size and self.x < tile.x + TILE_SIZE and self.y - self.speed < tile.y + TILE_SIZE and self.y - self.speed > tile.y):
                        return
        self.y -= self.speed

    def move_down(self, map_tiles):
        self.y += self.speed
    
    def move_left(self, map_tiles): 
        self.x -= self.speed

    def move_right(self, map_tiles):
        self.x += self.speed