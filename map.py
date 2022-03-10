from tiles import *

class Map():
  def __init__(self, sprite_sheet, SCALE):
    self.map = TileMap('map21x21.csv', sprite_sheet, SCALE)
    self.sprite_sheet = sprite_sheet
    self.SCALE = SCALE
    self.end = False

  def change_map(self):
    if self.end:
      return
    if self.map.filename == 'map21x21.csv':
      self.map = TileMap('map21x21(2).csv', self.sprite_sheet, self.SCALE)
    else:
      self.map = TileMap('map21x21.csv', self.sprite_sheet, self.SCALE)
    print(self.map.filename)
  
  def final_map(self):
    self.end = True
    self.map = TileMap('map21x21(3).csv', self.sprite_sheet, self.SCALE)
    print(self.map.filename)