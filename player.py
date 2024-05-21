import pygame

MAP_WIDTH = 70
MAP_HEIGHT = 50

TILE_SIZE = 64

PACE = 5
PACE_DANCE = 8
PACE_ROT = 8

PACE_PNJ = 1

WINDOW_WIDTH = TILE_SIZE*16
WINDOW_HEIGHT = TILE_SIZE*9

COLOR = (255, 100, 98) 
SURFACE_COLOR = (167, 255, 100) 

def dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + dim(a[0])


#Groups
class Game_Sprite ():
    all_sprites_list = pygame.sprite.Group() 
    me = pygame.sprite.RenderUpdates() 
    pnj = pygame.sprite.RenderUpdates()

class Sprite(pygame.sprite.Sprite): 
    def __init__(self, group): 
        super().__init__() 
#        self.images = images        # [front,back,left,right]
        self.index = 0              #for pace purposes
        self.animation = 0          #index of the animation image
        self.image = pygame.Surface((1,1))


class Pnj(Sprite):
    def __init__(self, group, x, y, images, x_size=32, y_size=52, mv_count=0):
        super().__init__(group)
        self.images = images
        self.x = x
        self.y = y 
        self.x_size = x_size
        self.y_size = y_size
        self.index = 0
        self.pace_count = 0
        self.dest =[x,y]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.add([Game_Sprite.all_sprites_list,group]) 
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.animation = 0

    def update_pos(self) :
        '''
        Change the position of the sprite based on the position specified to the move() function
        Return : (Bool) False if the sprite is already at destination
        '''
        x_move = 1
        y_move = 1
        if self.dest[0] < self.x :
            x_move = -1
        if self.dest[1] < self.y :
            y_move = -1
        if (self.dest[0] == self.x) and (self.dest[1] == self.y) :
            return False
        elif (self.dest[1] != self.y) :
            self.pace_count += 1
            if self.pace_count == PACE_PNJ :
                self.pace_count = 0
                self.y += y_move
                self.index += 1
                if self.index == PACE and len(self.images) > 5:
                    self.index = 0
                    self.animation += 1
                    if self.animation == 7 :
                        self.animation = 0
                    self.image = self.images[self.animation]
        elif (self.dest[0] != self.x) :
            self.pace_count += 1
            if self.pace_count == PACE_PNJ :
                self.pace_count = 0
                self.x += x_move
        self.rect.x = self.x - self.x_size//2
        self.rect.y = self.y - self.y_size//2
        return True

    def move(self,x,y) :
        self.dest = [x,y]

    def dance(self) :
        self.index += 1
        if self.index == PACE_DANCE :
            self.index = 0
            self.animation += 1
            if self.animation == 6 :
                self.animation = 0
        self.image = self.images[self.animation]

    def rot(self) :
        self.index += 1
        if self.index == PACE_ROT :
            self.index = 0
            self.animation += 1
            if self.animation == 4 :
                self.animation = 0
        self.image = self.images[self.animation]    

    def render_baby(self, window):
        # Calculate the position and size of the rectangle
        rect_width = self.x_size
        rect_height = self.y_size

        if self.x < WINDOW_WIDTH//2:
            self.rect.x = self.x - rect_width//2
        elif self.x > MAP_WIDTH*TILE_SIZE - WINDOW_WIDTH//2:
            self.rect.x = WINDOW_WIDTH + self.x - MAP_WIDTH*TILE_SIZE - rect_width//2
        else:
            self.rect.x = (WINDOW_WIDTH - rect_width) // 2
        if self.y < WINDOW_HEIGHT//2:
            self.rect.y = self.y - rect_height//2
        elif self.y > MAP_HEIGHT*TILE_SIZE - WINDOW_HEIGHT//2:
            self.rect.y = WINDOW_HEIGHT + self.y - MAP_HEIGHT*TILE_SIZE - rect_height//2
        else:
            self.rect.y = (WINDOW_HEIGHT - rect_height) // 2


class Perso(Sprite):
    def __init__(self, group, x, y, images, x_size=32, y_size=52, mv_count=0):
        super().__init__(group)
        self.images = images
        self.x = x
        self.y = y 
        self.x_size = x_size
        self.y_size = y_size
        self.speed = 10
        self.sign_sensitivity = 2
        self.image = self.images[0][0]
        self.rect = self.image.get_rect()
        self.add([Game_Sprite.all_sprites_list,group]) 
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.pyj = False

    def render(self, window):
        # Calculate the position and size of the rectangle
        rect_width = self.x_size
        rect_height = self.y_size

        if self.x < WINDOW_WIDTH//2:
            self.rect.x = self.x - rect_width//2
        elif self.x > MAP_WIDTH*TILE_SIZE - WINDOW_WIDTH//2:
            self.rect.x = WINDOW_WIDTH + self.x - MAP_WIDTH*TILE_SIZE - rect_width//2
        else:
            self.rect.x = (WINDOW_WIDTH - rect_width) // 2
        if self.y < WINDOW_HEIGHT//2:
            self.rect.y = self.y - rect_height//2
        elif self.y > MAP_HEIGHT*TILE_SIZE - WINDOW_HEIGHT//2:
            self.rect.y = WINDOW_HEIGHT + self.y - MAP_HEIGHT*TILE_SIZE - rect_height//2
        else:
            self.rect.y = (WINDOW_HEIGHT - rect_height) // 2

        # Draw the rectangle on the screen
        #pygame.draw.rect(window, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))

    def anim_crouch(self) :
        if (self.image != self.images[8][0]) and (self.image != self.images[8][1]) and (self.image != self.images[8][2]) and (self.image != self.images[8][3]) :
            self.animation = 0
            self.index = 0
        if self.animation >= 4 :
            return
        self.index += 1
        if self.index == 20 :
            self.index = 0
            self.animation += 1
        if self.animation == 4 :
            return
        self.image = self.images[8][self.animation]


    def move_up(self, map_tiles):
        for row in map_tiles:
            for tile in row:
                if tile.is_walkable() == False:
                    if (self.x - self.x_size//2 > tile.x*TILE_SIZE - self.x_size and self.x - self.x_size//2 < tile.x*TILE_SIZE + TILE_SIZE and self.y - self.y_size//2 - self.speed < tile.y*TILE_SIZE + TILE_SIZE and self.y - self.y_size//2 - self.speed > tile.y*TILE_SIZE):
                        self.y = tile.y*TILE_SIZE + TILE_SIZE + self.y_size//2
                        return
        self.index += 1
        if self.index == PACE :
            self.index = 0
            self.animation += 1
            if self.animation == 7 :
                self.animation = 0
        if self.pyj == False :
            self.image = self.images[1][self.animation]
        else :
            self.image = self.images[5][self.animation]
        self.y -= self.speed


    def move_down(self, map_tiles):
        for row in map_tiles:
            for tile in row:
                if tile.is_walkable() == False:
                    if (self.x - self.x_size//2 > tile.x*TILE_SIZE - self.x_size and self.x - self.x_size//2 < tile.x*TILE_SIZE + TILE_SIZE and self.y + self.y_size//2 + self.speed < tile.y*TILE_SIZE + TILE_SIZE and self.y + self.y_size//2 + self.speed > tile.y*TILE_SIZE):
                        self.y = tile.y*TILE_SIZE - self.y_size//2
                        return
        self.index += 1
        if self.index == PACE :
            self.index = 0
            self.animation += 1
            if self.animation == 7 :
                self.animation = 0
        if self.pyj == False :
            self.image = self.images[0][self.animation]
        else :
            self.image = self.images[4][self.animation]                    
        self.y += self.speed


    
    def move_left(self, map_tiles): 
        for row in map_tiles:
            for tile in row:
                if tile.is_walkable() == False:
                    if (self.y - self.y_size//2 > tile.y*TILE_SIZE - self.y_size and self.y - self.y_size//2 < tile.y*TILE_SIZE + TILE_SIZE and self.x - self.x_size//2 - self.speed < tile.x*TILE_SIZE + TILE_SIZE and self.x - self.x_size//2 - self.speed > tile.x*TILE_SIZE):
                        self.x = tile.x*TILE_SIZE + TILE_SIZE + self.x_size//2
                        return
        self.index += 1
        if self.index == PACE :
            self.index = 0
            self.animation += 1
            if self.animation == 7 :
                self.animation = 0
        if self.pyj == False :
            self.image = self.images[2][self.animation]
        else :
            self.image = self.images[6][self.animation]
        self.x -= self.speed


    def move_right(self, map_tiles):
        for row in map_tiles:
            for tile in row:
                if not tile.is_walkable():
                    if (self.y - self.y_size//2 > tile.y*TILE_SIZE - self.y_size and self.y - self.y_size//2 < tile.y*TILE_SIZE + TILE_SIZE and self.x + self.x_size//2 + self.speed < tile.x*TILE_SIZE + TILE_SIZE and self.x + self.x_size//2 + self.speed > tile.x*TILE_SIZE):
                        self.x = tile.x*TILE_SIZE - self.x_size//2
                        return
        self.index += 1
        if self.index == PACE :
            self.index = 0
            self.animation += 1
            if self.animation == 7 :
                self.animation = 0
        if self.pyj == False :
            self.image = self.images[3][self.animation]
        else :
            self.image = self.images[7][self.animation]
        self.x += self.speed
 

