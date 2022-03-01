import pygame

pygame.init()

WIDTH, HEIGHT = 900, 500   #in caps as they are constants

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

  run = True
  
  while run:

    for event in pygame.event.get():
      #this gets us all the events, loops through them and we can check what they were
      if event.type == pygame.QUIT:
        run = False

    #pygame.quit()

if __name__ == "__main__":
  main() 
