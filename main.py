import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

x=50
y=425
width=40
height=60
vel=5

run = True
while run:
  pygame.time.delay(100)
  #check for event
  for event in pygame.event.get():
    #loops through events
    if event.type == pygame.QUIT:
      #if you hit big red button in corner to close window, then 
      run=False

  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_LEFT] and x > vel:
    x -= vel
    #vel changes speed of movement
  if keys[pygame.K_RIGHT] and x < 500 - width - vel:
    #character not allowed to move off right of screen
    #width is the width of the character
    #the position of the character will not be allowed to move past the border now set the width of the character from the edge
    x += vel
  if keys[pygame.K_UP] and y > vel:
    y -= vel
  if keys[pygame.K_DOWN] and y < 500 - height - vel:
    y += vel
  
  win.fill((0, 0, 0))
  #this will fill the background with black so you don't see a trail of red rectangles

  pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
  pygame.display.update()

pygame.quit()
