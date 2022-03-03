import pygame
import spriteSheet

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('dungeon_sheet.png').convert_alpha()

sprite_sheet = spriteSheet.SpriteSheet(sprite_sheet_image)

BG = (50, 120, 50)

frame_0 = sprite_sheet.get_image(5, 16, 16, 4)
frame_1 = sprite_sheet.get_image(1, 16, 16, 4)
frame_2 = sprite_sheet.get_image(2, 16, 16, 4)
frame_192 = sprite_sheet.get_image(192, 16, 16, 4)
frame_29 = sprite_sheet.get_image(29, 16, 16, 4)
frame_53 = sprite_sheet.get_image(53, 16, 16, 4)

run = True
while run:

  screen.fill(BG)

  screen.blit(frame_0, (0,0))
  screen.blit(frame_192, (64,0))
  screen.blit(frame_192, (128,0))
  screen.blit(frame_1, (192,0))
  screen.blit(frame_1, (256,0))
  screen.blit(frame_1, (320,0))
  screen.blit(frame_1, (384,0))
  screen.blit(frame_2, (436, 0))
  screen.blit(frame_29, (0,64))
  screen.blit(frame_53, (0,128))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()