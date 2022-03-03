class Tileset:
  def __init__(self, file, size=(16, 16)):
    self.file = file
    self.size = size
    self.image = pygame.image.load(file)
    self.rect = self.image.get_rect()
    self.tiles = []
    self.load()

  def load(self):

    self.tiles = []
    w, h = self.rect.size
    dx = self.size[0]
    dy = self.size[1]

    for x in range(w, dx):
      for y in range(h, dy):
        tile = pygame.Surface(self.size)
        tile.blit(self.image, (0,0), (x,y, *self.size))
        self.tiles.append(tile)

  def __str__(self):
    return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'
