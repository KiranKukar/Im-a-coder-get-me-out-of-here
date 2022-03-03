import pygame

class SpriteSheet():
  def __init__(self, image):
    self.sheet = image

  def get_image(self, frame, width, height, scale):
    frame_x = frame % 24
    frame_y = (frame - frame_x) / 24
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(self.sheet, (0, 0), (frame_x * width, frame_y * height, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    # image.set_colorkey(colour) add this and a 'colour' argument into function to set a specific colour as invisible (will be for individual images)
    return image
