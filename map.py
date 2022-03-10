from tiles import *

class Map():
  def __init__(self, sprite_sheet, SCALE):
    self.map = TileMap('map21x21.csv', sprite_sheet, SCALE)
    self.sprite_sheet = sprite_sheet
    self.SCALE = SCALE

  def change_map(self):
    print(self.map.filename)
    if self.map.filename == 'map21x21.csv':
      self.map = TileMap('map21x21(2).csv', self.sprite_sheet, self.SCALE)
    else:
      self.map = TileMap('map21x21.csv', self.sprite_sheet, self.SCALE)