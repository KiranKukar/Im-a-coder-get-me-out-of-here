import pygame, sys
import button
import textwrap
# import main 

pygame.init()

SCALE = 2
BG = (185, 237, 214)
WIN_WIDTH = 336 * SCALE
WIN_HEIGHT = 336 * SCALE
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("I'm a Coder, Get Me Out of Here!")

#loads Main Menu button images
start_img = pygame.image.load('img/button-imgs/New Game.png').convert_alpha()
exit_img = pygame.image.load('img/button-imgs/Exit.png').convert_alpha()
about_img = pygame.image.load('img/button-imgs/About.png').convert_alpha()
credits_img = pygame.image.load('img/button-imgs/Credits.png').convert_alpha()

#Creates Main Menu button instances
start_button = button.Button(50, 300, start_img, 0.8)
exit_button = button.Button(370, 300, exit_img, 0.8)
about_button = button.Button(50, 500, about_img, 0.8)
credits_button = button.Button(370, 500, credits_img, 0.8)

font = pygame.font.SysFont('consolas', 60)
smallText = pygame.font.SysFont('consolas', 20)

story_text = """Hello Agent! Last night while out for drinks with your collegues at MI5 you overheard your coworker planning to bring down MI5 by scrambling the code in their firewalls. That’s the last thing you rememeber. You’ve woken up with a massive headache in the server room. The doors are locked and they’ve already sabotaged the code. They must have left you here to frame you. Can you fix the code to foil their plans and break your way out!"""


# clock = pygame.time.Clock()

class Menu():
    def __init__(self):
        self.main_menu()

    def wrap_text():
        # Wrap this text.
        wrapper = textwrap.TextWrapper(width=50)

        word_list = wrapper.wrap(text=story_text)

        # Print each line.
        for element in word_list:
            return (element)

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
            self.draw_header('main menu', font, (255, 255, 255), win, 375, 75)

            if start_button.draw(win):
                print('Start')
                self.instructions_screen()
            if exit_button.draw(win):
                pygame.quit()
                sys.exit()
            if about_button.draw(win):
                print('About')
                self.about_screen()
            if credits_button.draw(win):
                print ('Credits')
                self.credits_sreen()
    
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

    def instructions_screen(self):
        while True:
            import main
            win.fill((0,0,0))
            self.draw_header('instructions:', font, (255, 255, 255), win, 500, 75)
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
            # clock.tick(60)

    def about_screen(self, element):
        while True:
            win.fill((0,0,0))
            self.draw_header(element, font, (255, 255, 255), win, 400, 75)
            # draw_text(story_text, smallText, (255, 255, 255), win, 20, 600)

            mx, my = pygame.mouse.get_pos()

            
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
            # clock.tick(60)

    def credits_sreen(self):
        while True:
            win.fill((0,0,0))
            self.draw_header('Credits:', font, (255, 255, 255), win, 300, 100)
            self.draw_header('Alex', smallText, (255, 255, 255), win, 78, 200)
            self.draw_header('Elliott', smallText, (255, 255, 255), win, 97, 300)
            self.draw_header('Esther', smallText, (255, 255, 255), win, 90, 400)
            self.draw_header('Haydn', smallText, (255, 255, 255), win, 85, 500)
            self.draw_header('Kiran', smallText, (255, 255, 255), win, 80, 600)
            self.draw_header('Saad', smallText, (255, 255, 255), win, 78, 700)

            # pos = pygame.mouse.get_pos()
	        #     print(pos)

            mx, my = pygame.mouse.get_pos()

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
            # clock.tick(60)
