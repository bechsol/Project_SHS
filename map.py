from pytmx import TiledMap
import pygame

from player import Perso
from player import Game_Sprite as GS


# Constants

MAP_WIDTH = 30
MAP_HEIGHT = 20

WINDOW_WIDTH = 64*16
WINDOW_HEIGHT = 64*9

TILE_SIZE = 64

SCALE_FACTOR = 2

sprite1 = pygame.image.load("pixil-frame-0.png")

class Scene:
    def __init__(self, map_filename):
        self.map = Map(MAP_WIDTH, MAP_HEIGHT)
        self.map.load_tmx(map_filename)
        #self.player = Player(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        self.player = Perso(GS.me,WINDOW_WIDTH//2, WINDOW_HEIGHT//2,sprite1)

        self.filter1 = Filter((WINDOW_WIDTH, WINDOW_HEIGHT), (0, 0, 0), speed=1)
        self.filter1.enabled = False

        self.filter2 = Filter((WINDOW_WIDTH, WINDOW_HEIGHT), (0, 0, 0), speed=0.05)
        self.filter2.enabled = False

        # For displaying text on the screen
        self.font = pygame.font.Font(None, 36)  # Font for the sign text
        self.text_color = (255, 255, 255)  # White text color
        self.background_color = (139, 69, 19)  # Brown background color
        self.display_text = False
        self.text_to_display = "Error: Text not set!"
    
    def handle_input(self):
        self.filter1.update_animation()
        self.filter2.update_animation()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if not self.display_text:
                self.player.move_up(self.map.tiles)
        if keys[pygame.K_DOWN]:
            if not self.display_text:
                self.player.move_down(self.map.tiles)
        if keys[pygame.K_LEFT]:
            if not self.display_text:
                self.player.move_left(self.map.tiles)
        if keys[pygame.K_RIGHT]:
            if not self.display_text:
                self.player.move_right(self.map.tiles)
        if keys[pygame.K_SPACE]:
            self.filter1.enable()
            for tile in self.map.interactable_tiles:
                if (self.player.x - self.player.x_size//2 > tile.x*TILE_SIZE - self.player.x_size - self.player.sign_sensitivity and self.player.x - self.player.x_size//2 < tile.x*TILE_SIZE + TILE_SIZE + self.player.sign_sensitivity and self.player.y - self.player.y_size//2 > tile.y*TILE_SIZE - self.player.y_size - self.player.sign_sensitivity and self.player.y - self.player.y_size//2 < tile.y*TILE_SIZE + TILE_SIZE + self.player.sign_sensitivity):
                    interact_type, interact_data = tile.interact()
                    if interact_type == "sign":
                        self.display_text = True
                        self.text_to_display = interact_data
        if keys[pygame.K_ESCAPE]:
            self.display_text = False
            self.filter1.disable()

        if keys[pygame.K_RETURN]:
            if self.filter2.enabled and not self.filter2.is_animating():
                self.filter2.disable()
            elif not self.filter2.enabled and not self.filter2.is_animating():   
                self.filter2.enable()
    
    def render(self, window):
        self.map.render(window, (self.player.x - WINDOW_WIDTH//2, self.player.y - WINDOW_HEIGHT//2))
        self.player.render(window)
        GS.me.update()
        GS.me.draw(window)
        if not self.filter2.enabled:
            self.filter1.apply(window)
        if not self.filter1.enabled:
            self.filter2.apply(window)
        if self.display_text:
            self.show_text(window, self.text_to_display)
        

    def show_text(self, window, text):
        # Create a rectangle for the background
        text_surface = self.font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        
        background_rect = pygame.Rect(0, 0, text_rect.width + 20, text_rect.height + 20)  # Adjust size as needed
        background_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        # Draw shadow-like effect
        shadow_offset = 3
        shadow_rect = background_rect.move(shadow_offset, shadow_offset)
        pygame.draw.rect(window, (0, 0, 0), shadow_rect)

        # Draw background rectangle
        pygame.draw.rect(window, self.background_color, background_rect)

        # Render text
        text_rect.center = background_rect.center
        window.blit(text_surface, text_rect)

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]
        self.interactable_tiles = []

    def load_tmx(self, filename):

        tmxdata = TiledMap(filename)
        


        for x in range(tmxdata.width):  
            for y in range(tmxdata.height):
                im = tmxdata.get_tile_image(x, y, 0)
                gid = tmxdata.get_tile_gid(x, y, 0)

                if im != None:
                    if tmxdata.get_tile_properties_by_gid(gid)["type"] == "Sign":
                        self.tiles[y][x] = Sign(x, y, im, "Hello I am a sign!")
                        self.interactable_tiles.append(self.tiles[y][x])
                    elif tmxdata.get_tile_properties_by_gid(gid)["type"] == "Wall":
                        self.tiles[y][x] = Wall(x, y, im)
                    else:
                        self.tiles[y][x] = Floor(x, y, im)
        

    def render(self, window, offset=(0, 0)):
        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    tile.render(window, offset)

class Filter:
    def __init__(self, window_size, color, speed=0.05):
        self.window_size = window_size
        self.color = color
        self.speed = speed
        self.enabled = False
        self.animation_progress = 1
        self.direction = "in"
        self.animating = False

    def apply(self, window):
        if self.enabled or self.is_animating():
            # Create a grayscale surface of the same size as the window
            gray_surface = pygame.Surface(self.window_size).convert()
            gray_surface.fill((128, 128, 128))  # Fill with gray color
            gray_surface.set_alpha(int(128 * self.animation_progress))  # Set transparency to 128 (50% opacity)

            # Blit the grayscale surface onto the window
            window.blit(gray_surface, (0, 0))

    def update_animation(self):
        # Update animation progress based on direction and speed
        if self.direction == "in":
            self.animation_progress += self.speed
        elif self.direction == "out":
            self.animation_progress -= self.speed
        

        # Clamp animation progress to [0, 1]
        self.animation_progress = max(0, min(1, self.animation_progress))


        self.animating = self.animation_progress > 0 and self.animation_progress < 1

    def enable(self):
        if self.enabled == False:
            self.direction = "in"
            self.animation_progress = 0
            self.enabled = True

    def disable(self):
        if self.enabled == True:
            self.direction = "out"
            self.animation_progress = 1
            self.enabled = False

    def is_animating(self):
        return self.animating

    


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

class Wall_Fence_1(Wall):
    def __init__(self, x, y, image_data):
        super().__init__(x, y, image_data)


class Interactable(Tile):
    def __init__(self, walkable, x, y, image_data):
        super().__init__(walkable, x, y, image_data)

    def interact(self):
        pass

class Sign(Interactable):
    def __init__(self, x, y, image_data, message):
        super().__init__(False, x, y, image_data)
        self.message = message

    def interact(self):
        return "sign", self.message

class Floor(Tile):
    def __init__(self, x, y, image_data):
        super().__init__(True, x, y, image_data)


class Door(Tile):
    def __init__(self, x, y, image_data):
        super().__init__(True, x, y, image_data)

    def interact(self, player_x, player_y, player_direction):
        if (player_x*TILE_SIZE < self.x*TILE_SIZE + TILE_SIZE and player_x*TILE_SIZE > self.x*TILE_SIZE - TILE_SIZE) and (player_y*TILE_SIZE < self.y*TILE_SIZE + TILE_SIZE and player_y*TILE_SIZE > self.y*TILE_SIZE - TILE_SIZE):
            print("You opened the door!")