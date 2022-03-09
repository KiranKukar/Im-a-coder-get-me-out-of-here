import pygame, csv, os

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
  def __init__(self, filename, sprite_sheet, scale):
    self.tile_size = 16
    self.scale = scale
    self.sprite_sheet = sprite_sheet
    self.tile_group = pygame.sprite.Group()
    self.laptop_group = pygame.sprite.Group()
    self.laptop1 = pygame.sprite.Group()
    self.laptop2 = pygame.sprite.Group()
    self.laptop3 = pygame.sprite.Group()
    self.laptop4 = pygame.sprite.Group()
    self.laptop5 = pygame.sprite.Group()
    self.laptop6 = pygame.sprite.Group()
    self.exit_door = pygame.sprite.Group()

    # starting coordinates of player sprite
    self.start_x, self.start_y = 0, 0 
    # self.image = image

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
        if tile != '-1':
          image = self.sprite_sheet.get_image(int(tile), self.tile_size, self.tile_size, self.scale)
          tile_item = Tile(image, x * self.tile_size * self.scale, y * self.tile_size * self.scale)
          tiles.append(tile_item)
          if tile == '158':
            self.laptop_group.add(tile_item)
            self.laptop1.add(tile_item)
          elif tile == '157':
            self.laptop_group.add(tile_item)
            self.laptop2.add(tile_item)
          elif tile == '153':
            self.laptop_group.add(tile_item)
            self.laptop3.add(tile_item)
          elif tile == '154':
            self.laptop_group.add(tile_item)
            self.laptop4.add(tile_item)
          elif tile == '161':
            self.laptop_group.add(tile_item)
            self.laptop5.add(tile_item)
          elif tile == '162':
            self.laptop_group.add(tile_item)
            self.laptop6.add(tile_item)
          elif tile == '148':
            self.exit_door.add(tile_item)
          else:
            self.tile_group.add(tile_item)
        # Move to next tile in current row
        x +=1
      # Move to next row  
      y += 1
    
    # Store the size of the tile map
    self.map_w, self.map_h = x * self.tile_size * self.scale, y * self.tile_size * self.scale
    return tiles

    # frame_0 = self.sprite_sheet.get_image(tile, self.tile_size, self.tile_size, self.scale)

