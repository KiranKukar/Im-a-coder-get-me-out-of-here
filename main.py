import pygame

pygame.init()

WIDTH, HEIGHT = 900, 500   #in caps as they are constants

from pygame.locals import (
  RLEACCEL, # does something to allow uploaded images to render on the screen
)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


background_surface = pygame.image.load("hacker.jpeg").convert()
background_surface = pygame.transform.scale(background_surface, (WIDTH, HEIGHT))


#define the main function for the game
def main():

  run = True
  
  while run:

    for event in pygame.event.get():
      #this gets us all the events, loops through them and we can check what they were
      if event.type == pygame.QUIT:
        run = False

    WINDOW.blit(background_surface, (0,0))

    #pygame.quit()
    pygame.display.flip()

if __name__ == "__main__":
  main() 
