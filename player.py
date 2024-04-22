import pygame

MAP_WIDTH = 30
MAP_HEIGHT = 20

TILE_SIZE = 64

WINDOW_WIDTH = TILE_SIZE*16
WINDOW_HEIGHT = TILE_SIZE*9

COLOR = (255, 100, 98) 
SURFACE_COLOR = (167, 255, 100) 



#Groups
class Game_Sprite ():
    all_sprites_list = pygame.sprite.Group() 
    me = pygame.sprite.RenderUpdates() 

class Sprite(pygame.sprite.Sprite): 
    def __init__(self, group, images): 
        super().__init__() 
        self.images = images
        self.index = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.add([Game_Sprite.all_sprites_list,group]) 
        self.rect = self.image.get_rect() 

class Perso(Sprite):
    def __init__(self, group, x, y, images, x_size=64, y_size=64, mv_count=0):
        super().__init__(group, images)
        self.x = x
        self.y = y 
        self.rect.x = x
        self.rect.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.speed = 3
        self.sign_sensitivity = 2


    def render(self, window):
        # Calculate the position and size of the rectangle
        rect_width = self.x_size
        rect_height = self.y_size

        if self.x < WINDOW_WIDTH//2:
            self.rect.x = self.x - rect_width//2
        elif self.x > MAP_WIDTH*TILE_SIZE - WINDOW_WIDTH//2:
            self.rect.x = WINDOW_WIDTH + self.x - MAP_WIDTH*TILE_SIZE - rect_width//2
        else:
    #        print(self.x_size.get_width())
            self.rect.x = (WINDOW_WIDTH - rect_width) // 2
        if self.y < WINDOW_HEIGHT//2:
            self.rect.y = self.y - rect_height//2
        elif self.y > MAP_HEIGHT*TILE_SIZE - WINDOW_HEIGHT//2:
            self.rect.y = WINDOW_HEIGHT + self.y - MAP_HEIGHT*TILE_SIZE - rect_height//2
        else:
            self.rect.y = (WINDOW_HEIGHT - rect_height) // 2

        # Draw the rectangle on the screen
        #pygame.draw.rect(window, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))

    def move_up(self, map_tiles):
        for row in map_tiles:
            for tile in row:
                if tile.is_walkable() == False:
                    if (self.x - self.x_size//2 > tile.x*TILE_SIZE - self.x_size and self.x - self.x_size//2 < tile.x*TILE_SIZE + TILE_SIZE and self.y - self.y_size//2 - self.speed < tile.y*TILE_SIZE + TILE_SIZE and self.y - self.y_size//2 - self.speed > tile.y*TILE_SIZE):
                        self.y = tile.y*TILE_SIZE + TILE_SIZE + self.y_size//2
                        return
        self.index = 1
        self.image = self.images[self.index]
        self.y -= self.speed


    def move_down(self, map_tiles):
        for row in map_tiles:
            for tile in row:
                if tile.is_walkable() == False:
                    if (self.x - self.x_size//2 > tile.x*TILE_SIZE - self.x_size and self.x - self.x_size//2 < tile.x*TILE_SIZE + TILE_SIZE and self.y + self.y_size//2 + self.speed < tile.y*TILE_SIZE + TILE_SIZE and self.y + self.y_size//2 + self.speed > tile.y*TILE_SIZE):
                        self.y = tile.y*TILE_SIZE - self.y_size//2
                        return
        self.index = 0
        self.image = self.images[self.index]                        
        self.y += self.speed


    
    def move_left(self, map_tiles): 
        for row in map_tiles:
            for tile in row:
                if tile.is_walkable() == False:
                    if (self.y - self.y_size//2 > tile.y*TILE_SIZE - self.y_size and self.y - self.y_size//2 < tile.y*TILE_SIZE + TILE_SIZE and self.x - self.x_size//2 - self.speed < tile.x*TILE_SIZE + TILE_SIZE and self.x - self.x_size//2 - self.speed > tile.x*TILE_SIZE):
                        self.x = tile.x*TILE_SIZE + TILE_SIZE + self.x_size//2
                        return
        self.index = 2
        self.image = self.images[self.index]  
        self.x -= self.speed


    def move_right(self, map_tiles):
        for row in map_tiles:
            for tile in row:
                if not tile.is_walkable():
                    if (self.y - self.y_size//2 > tile.y*TILE_SIZE - self.y_size and self.y - self.y_size//2 < tile.y*TILE_SIZE + TILE_SIZE and self.x + self.x_size//2 + self.speed < tile.x*TILE_SIZE + TILE_SIZE and self.x + self.x_size//2 + self.speed > tile.x*TILE_SIZE):
                        self.x = tile.x*TILE_SIZE - self.x_size//2
                        return
        self.index = 3
        self.image = self.images[self.index]  
        self.x += self.speed
 

