from pytmx import TiledMap
import pygame


# Constants

MAP_WIDTH = 30
MAP_HEIGHT = 20

WINDOW_WIDTH = 64*16
WINDOW_HEIGHT = 64*9

TILE_SIZE = 64

SCALE_FACTOR = 2



class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]

    def load_tmx(self, filename):

        tmxdata = TiledMap(filename)
        


        for x in range(tmxdata.width):  
            for y in range(tmxdata.height):
                im = tmxdata.get_tile_image(x, y, 0)
                gid = tmxdata.get_tile_gid(x, y, 0)

                if im != None:
                    if gid == 1:
                        self.tiles[y][x] = Wall_Fence_1(x, y, im)
                    else:
                        self.tiles[y][x] = Floor(x, y, im)
        

    def render(self, window, offset=(0, 0)):
        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    tile.render(window, offset)



class Tile:
    def __init__(self, walkable, x, y, image_data):
        self.walkable = walkable
        self.x = x 
        self.y = y
        image_path, (image_x, image_y, image_width, image_height), _ = image_data
        original_image = pygame.image.load(image_path)
        cropped_image = self.crop_image(original_image, image_x, image_y, image_width, image_height)
        scaled_image = pygame.transform.scale(cropped_image, (image_width * 2, image_height * 2))
        self.image = scaled_image
    
    def crop_image(self, image, x, y, width, height):
        cropped_rect = pygame.Rect(x, y, width, height)
        cropped_image = pygame.Surface(cropped_rect.size)
        cropped_image.blit(image, (0, 0), cropped_rect)
        return cropped_image
    
    def render(self, window, offset=(0, 0)):
        offset = (min(offset[0], TILE_SIZE*MAP_WIDTH-WINDOW_WIDTH), min(offset[1], TILE_SIZE*MAP_HEIGHT-WINDOW_HEIGHT))
        offset = (max(offset[0], 0), max(offset[1], 0))
        window.blit(self.image, (self.x * TILE_SIZE - offset[0], self.y * TILE_SIZE - offset[1]))

    def is_walkable(self):
        return self.walkable


class Wall(Tile):
    def __init__(self, x, y, image_data):
        super().__init__(False, x, y, image_data)

class Wall_Fence_1(Tile):
    def __init__(self, x, y, image_data):
        super().__init__(False, x, y, image_data)



class Floor(Tile):
    def __init__(self, x, y, image_data):
        super().__init__(True, x, y, image_data)


class Door(Tile):
    def __init__(self, x, y, image_data):
        super().__init__(True, x, y, image_data)

    def interact(self, player_x, player_y, player_direction):
        if (player_x*TILE_SIZE < self.x*TILE_SIZE + TILE_SIZE and player_x*TILE_SIZE > self.x*TILE_SIZE - TILE_SIZE) and (player_y*TILE_SIZE < self.y*TILE_SIZE + TILE_SIZE and player_y*TILE_SIZE > self.y*TILE_SIZE - TILE_SIZE):
            print("You opened the door!")