import pygame
import button

#Create screen display
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Im-a-coder-get-me-out-of-here')
# image = Image.open("Pixel background.tiff")
background = pygame.image.load("Pixel background.png")

#load button images
start_img = pygame.image.load('img/button-imgs/New Game.png').convert_alpha()
exit_img = pygame.image.load('img/button-imgs/Exit.png').convert_alpha()
about_img = pygame.image.load('img/button-imgs/About.png').convert_alpha()
credits_img = pygame.image.load('img/button-imgs/Credits.png').convert_alpha()

#Creating button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)
about_button = button.Button(100, 400, about_img, 0.8)
credits_button = button.Button(450, 400, credits_img, 0.8)

#Game Loop
run = True
while run:

  screen.fill((202, 228, 241))
  screen.blit(background(600, 800))
  screen.blit(background, [0, 0])

  if start_button.draw(screen):
    print('Start')
  if exit_button.draw(screen):
    run = False
    print ('Exit')
  if about_button.draw(screen):
    print('About')
  if credits_button.draw(screen):
    print ('Credits')

    #Event Handler
  for event in pygame.event.get():
        #Quit game
      if event.type == pygame.QUIT:
          run = False
    #Update the game window at each iteration of the code. 
  pygame.display.update()

pygame.quit()
      