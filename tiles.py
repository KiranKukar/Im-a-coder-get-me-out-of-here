import pygame, csv, os, pytmx

class Tile(pygame.sprite.Sprite):
  def __init__(self, image, x, y):

    # Initiates Sprite class
    pygame.sprite.Sprite.__init__(self)

    # Load in image
    self.image = image

    # Store image in rectangle object (and assign x, y coordinates)
    self.rect = self.image.get_rect()
    self.rect.x, self.rect.y = x, y

  
  # helper function to draw tile
  def draw(self, surface):

    # blitting tile image onto surface based on x, y coordinates of rect
    surface.blit(self.image, (self.rect.x, self.rect.y))

class TileMap():
  def __init__(self, filename, tmxfile):
    self.tile_size = 16

    # starting coordinates of player sprite
    self.start_x, self.start_y = 0, 0 
    # self.image = image

    # import tmx file
    tm = pytmx.load_pygame(tmxfile, pixelalpha=True)
    self.tmxdata = tm

    # runs load tiles function
    self.tiles = self.load_tiles(filename)

    # Creates map surface
    self.map_surface = pygame.Surface((self.map_w, self.map_h))
    self.map_surface.set_colorkey((0, 0, 0))
    self.load_map()

  def draw_map(self, surface):
    surface.blit(self.map_surface, (0, 0))

  def load_map(self):
    for tile in self.tiles:
      tile.draw(self.map_surface)

  # reads csv file
  def read_csv(self, filename):
    map = []
    with open(os.path.join(filename)) as data:
      data = csv.reader(data, delimiter=',')
      for row in data:
        map.append(list(row))
    return map

  # loads tiles
  def load_tiles(self, filename):
    tiles = []
    map = self.read_csv(filename)
    x, y = 0, 0
    for row in map:
      x = 0
      for tile in row:
        print(x, y)

        if tile == '-1':
          self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
        else:
          print(self.tmxdata.get_tile_gid(x, y, 0))
          tiles.append(Tile(self.tmxdata.get_tile_image_by_gid(self.tmxdata.get_tile_gid(x, y, 0)), x * self.tile_size, y * self.tile_size))
        # Move to next tile in current row
        x +=1
      # Move to next row  
      y += 1
    
    # Store the size of the tile map
    self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
    return tiles
      





# image = pygame.image.load('./dungeon_sheet.png')




