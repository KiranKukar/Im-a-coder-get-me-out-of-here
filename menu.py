import pygame, sys
import button
import textwrap
# import main 

pygame.init()

SCALE = 2
BG = (185, 237, 214)
win = pygame.display.set_mode((336 * SCALE, 336 * SCALE))

#loads Main Menu button images
start_img = pygame.image.load('img/button-imgs/New Game.png').convert_alpha()
exit_img = pygame.image.load('img/button-imgs/Exit.png').convert_alpha()
about_img = pygame.image.load('img/button-imgs/About.png').convert_alpha()
credits_img = pygame.image.load('img/button-imgs/Credits.png').convert_alpha()

#Creates Main Menu button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)
about_button = button.Button(100, 400, about_img, 0.8)
credits_button = button.Button(450, 400, credits_img, 0.8)

font = pygame.font.SysFont('consolas', 20)
# smallText = pygame.font.SysFont('consolas', 10)

story_text = "Hello Agent! Last night while out for drinks with your collegues at MI5 you overheard your coworker planning to bring down MI5 by scrambling the code in their firewalls. That’s the last thing you rememeber. You’ve woken up with a massive headache in the server room. The doors are locked and they’ve already sabotaged the code. They must have left you here to frame you. Can you fix the code to foil their plans and break your way out!"

# first_stage_story = story_text.splitlines()
first_stage_story = textwrap.wrap(story_text)

clock = pygame.time.Clock()

class Menu():
    def __init__(self):
        self.main_menu()

    def draw_header(self, text, font, colour, surface, x, y):
        textobj = font.render(text, 1, colour) 
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        textrect.center = (x // 2, y // 2)
        surface.blit(textobj, textrect)

    # def draw_text(text, smallText, colour, surface, x, y):
    #     textobj = smallText.render(text, 1, colour) 
    #     textrect = textobj.get_rect()
    #     textrect.center = (x // 2, y // 2)
    #     surface.blit(textobj, textrect)


    def main_menu(self):
        while True:
            # import main
            win.fill((0,0,0))
            self.draw_header('main menu', font, (255, 255, 255), win, 20, 20)

            if start_button.draw(win):
                print('Start')
                self.first_screen()
            if exit_button.draw(win):
                pygame.quit()
                sys.exit()
            if about_button.draw(win):
                print('About')
            if credits_button.draw(win):
                print ('Credits')
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            # clock.tick(60)

    def first_screen(self):
        while True:
            import main
            win.fill((0,0,0))
            self.draw_header('instructions:', font, (255, 255, 255), win, 20, 20)
            # draw_text(story_text, smallText, (255, 255, 255), win, 20, 600)

            mx, my = pygame.mouse.get_pos()

            if start_button.draw(win):
                print('Start')
                main.game()
            if exit_button.draw(win):
                self.main_menu()
    
            # button_1 = pygame.Rect(50, 100, 200, 50)
            # textSurf, textRect = button_1("Start game!", smallText)
            # textRect.center = ( (150+(100/2)), (450+(50/2)) )
            # gameDisplay.blit(textSurf, textRect)

            # button_2 = pygame.Rect(50, 200, 200, 50)
            # #This is to select the box with your mouse.
            # if button_1.collidepoint((mx, my)):
            #     if click:
            #         game()
            # if button_2.collidepoint((mx, my)):
            #     if click:
            #         main_menu()
            # pygame.draw.rect(win, (255, 0, 0), button_1)
            # pygame.draw.rect(win, (255, 0, 0), button_2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            
            pygame.display.update()
            clock.tick(60)
