import pygame

file = 'dungeon_sheet.png'
background_surface = pygame.image.load(file)
rect = background_surface.get_rect()
print(background_surface)

pygame.init()
screen = pygame.display.set_mode(rect.size)

screen.blit(background_surface, rect)
pygame.display.update()

while True:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()