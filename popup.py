import pygame
import pygamepopup
from pygamepopup.components import Button, InfoBox, TextElement
from pygamepopup.menu_manager import MenuManager

import pygame as pg


def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()


import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)



def main():
    clock = pg.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


class MainMenuScene:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.menu_manager = MenuManager(screen)
        self.exit_request = False

        self.create_main_menu_interface()

    def create_main_menu_interface(self):
        main_menu = InfoBox(
            "Main Menu",
            [
                [
                    Button(
                        title="Open other menu",
                        callback=lambda: self.create_other_menu(),
                    )
                ],
                [Button(title="Exit", callback=lambda: self.exit())],
            ],
            has_close_button=False,
        )
        self.menu_manager.open_menu(main_menu)

    def create_other_menu(self):
        other_menu = InfoBox(
            "Smaller menu",
            [
                [
                    TextElement(
                        text="The text content of a menu is automatically splitted in multiple "
                        "part "
                        "to fit in the box. To add a new paragraph, just create another "
                        "TextElement."
                    )
                ]
            ],
            width=300,
        )
        self.menu_manager.open_menu(other_menu)

    def exit(self):
        self.exit_request = True

    def display(self) -> None:
        self.menu_manager.display()

    def motion(self, position: pygame.Vector2) -> None:
        self.menu_manager.motion(position)

    def click(self, button: int, position: pygame.Vector2) -> bool:
        self.menu_manager.click(button, position)
        return self.exit_request


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Main Menu Example")

    pygamepopup.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    main_menu_scene = MainMenuScene(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                main_menu_scene.motion(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    running = not main_menu_scene.click(event.button, event.pos)
        screen.fill(pygame.Color("black"))
        main_menu_scene.display()
        pygame.display.update()
    pygame.quit()
    exit()


if __name__ == "__main__":
    main()